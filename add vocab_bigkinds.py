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
    'SEED':42
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

# 추가할 vocab 데이터
news_vocab = pd.read_csv("news_vocab.csv", encoding='cp949')
vocab_list = news_vocab['특성추출(가중치순 상위 50개)'].str.split(",")

# 추가할 vocab list 생성
vocab_list = sum(vocab_list, [])

# 사전학습된 모델 및 토크나이저
model_type = "klue/roberta-small"
tokenizer = AutoTokenizer.from_pretrained(model_type)
model = AutoModel.from_pretrained(model_type)

# 추가할 vocab list에서 기존 vocab 제외
new_tokens = set(vocab_list) - set(tokenizer.vocab.keys())
# vocab 추가
tokenizer.add_tokens(list(new_tokens))
# token embedding resize
model.resize_token_embeddings(len(tokenizer))
