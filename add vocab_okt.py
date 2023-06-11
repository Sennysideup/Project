# library
import pandas as pd
import numpy as np
import torch
import os
import random
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer, AutoModel
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch import nn
from tqdm import tqdm
from konlpy.tag import Okt

# setting
def seed_everything(seed):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = True
CFG = {
    'EPOCHS':20,
    'LEARNING_RATE':1e-5,
    'BATCH_SIZE':32,
    'SEED':41
}
seed_everything(CFG['SEED']) # Seed 고정
device = torch.device('cuda')

# 데이터 준비
train_original = pd.read_csv('data/train.csv')
train_original.drop(columns=['ID'], inplace=True)
test = pd.read_csv('data/test.csv')
test.drop(columns=['ID'], inplace=True)
submission = pd.read_csv('data/sample_submission.csv')

# 데이터 나누기
train, val, _, _ = train_test_split(train_original, train_original['label'], test_size=0.2, random_state=CFG['SEED'])
train = train.reset_index(drop=True)
val = val.reset_index(drop=True)

# Okt 적용
okt = Okt()
train['okt'] = [okt.morphs(s) for s in train['문장']]

# 추가할 vocab list 생성
vocab_list = sum(train['okt'], [])

# 사전학습된 모델 불러오기
model_type = "klue/roberta-small"
tokenizer = AutoTokenizer.from_pretrained(model_type)
model = AutoModel.from_pretrained(model_type)

# 생성한 vocab list에서 기존 vocab에 있는 단어 제외
new_tokens = set(vocab_list) - set(tokenizer.vocab.keys())
# vocab 추가
tokenizer.add_tokens(list(new_tokens))
# token embedding reize
model.resize_token_embeddings(len(tokenizer))
