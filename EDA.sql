-- EDA : 데이터 특징
-- 0. 캠페인 아이디별 개수 확인
SELECT
  count(DISTINCT ad_id) AS cnt_ad,
  count(DISTINCT fb_campaign_id) AS cnt_fb,
  count(DISTINCT xyz_campaign_id) AS cnt_xyz
FROM
  tutorial.kag_conversion_data

-- 1.1 ad_id별 타겟 성별 분포 확인
SELECT ad_id, count(distinct gender) as ad_cnt_gender
FROM tutorial.kag_conversion_data
group BY ad_id
order by cnt_gender desc

-- 1.2 fb_campaign_id별 타겟 성별 분포 확인
SELECT fb_campaign_id, count(distinct gender) as fb_cnt_gender
FROM tutorial.kag_conversion_data
group BY fb_campaign_id
order by fb_cnt_gender desc

-- 1.3 xyz_campaign_id별 타겟 성별 분포 확인
SELECT xyz_campaign_id, count(distinct gender) as xyz_cnt_gender
FROM tutorial.kag_conversion_data
group BY xyz_campaign_id
order by xyz_cnt_gender desc

-- 2.1 ad_id별 타겟 연령대 분포 확인
SELECT ad_id, count(distinct age) as ad_cnt_age
FROM tutorial.kag_conversion_data
group BY ad_id
order by ad_cnt_age desc

-- 2.2 fb_campaign_id별 타겟 연령대 분포 확인
SELECT fb_campaign_id, count(distinct age) as fb_cnt_age
FROM tutorial.kag_conversion_data
group BY fb_campaign_id
order by fb_cnt_age desc

-- 2.3 xyz_campaign_id별 타겟 연령대 분포 확인
SELECT xyz_campaign_id, count(distinct age) as xyz_cnt_age
FROM tutorial.kag_conversion_data
group BY xyz_campaign_id
order by xyz_cnt_age desc

-- 3.1 ad_id별 성별X연령대 분포 확인
SELECT ad_id, gender, age, count(1) as ad_cnt
FROM tutorial.kag_conversion_data
group BY ad_id, gender, age
order by ad_cnt desc

-- 3.2 fb_campaign_id별 타겟 성별X연령대 분포 확인
SELECT fb_campaign_id, gender, age, count(1) as fb_cnt
FROM tutorial.kag_conversion_data
group BY fb_campaign_id, gender, age
order by fb_cnt desc

-- 3.3 xyz_campaign_id별 타겟 성별X연령대 분포 확인
SELECT xyz_campaign_id, gender, age, count(1) as xyz_cnt
FROM tutorial.kag_conversion_data
group BY xyz_campaign_id, gender, age
order by xyz_cnt desc

-- 4.1 ad_id별 타겟 관심사 분포 확인
SELECT ad_id, count(distinct interest) as ad_cnt_interest
FROM tutorial.kag_conversion_data
group BY ad_id
order by ad_cnt_interest desc

-- 4.2 fb_campaign_id별 타겟 관심사 분포 확인
SELECT fb_campaign_id, count(distinct interest) as fb_cnt_interest
FROM tutorial.kag_conversion_data
group BY fb_campaign_id
order by fb_cnt_interest desc

-- 4.3 xyz_campaign_id별 타겟 관심사 분포 확인
SELECT xyz_campaign_id, count(distinct interest) as xyz_cnt_interest
FROM tutorial.kag_conversion_data
group BY xyz_campaign_id
order by xyz_cnt_interest desc

-- 5.1 ad_id별 타겟 성별X연령대X관심사 분포 확인
SELECT ad_id, gender, age, interest, count(1) as ad_cnt
FROM tutorial.kag_conversion_data
group BY ad_id, gender, age, interest
order by ad_cnt desc

-- 5.2 fb_campaign_id별 타겟 성별X연령대X관심사 분포 확인
SELECT fb_campaign_id, gender, age, interest, count(1) as fb_cnt
FROM tutorial.kag_conversion_data
group BY fb_campaign_id, gender, age, interest
order by fb_cnt desc

-- 5.3 xyz_campaign_id별 타겟 성별X연령대X관심사 분포 확인
SELECT xyz_campaign_id, gender, age, interest, count(1) as xyz_cnt
FROM tutorial.kag_conversion_data
group BY xyz_campaign_id, gender, age, interest
order by xyz_cnt desc

-- EDA : 광고별 주요 변수 기술통계량
-- 1. 노출 수 기술통계량
SELECT
  min(impressions),
  PERCENTILE_CONT(0.25) WITHIN GROUP (
    ORDER BY
      impressions
  ) AS Q1,
  PERCENTILE_CONT(0.5) WITHIN GROUP (
    ORDER BY
      impressions
  ) AS median,
	avg(impressions) as mean,
  PERCENTILE_CONT(0.75) WITHIN GROUP (
    ORDER BY
      impressions
  ) AS Q3,
  max(impressions)
FROM
  tutorial.kag_conversion_data

-- 2. 클릭 수 기술통계량
SELECT
  min(clicks),
  PERCENTILE_CONT(0.25) WITHIN GROUP (
    ORDER BY
      clicks
  ) AS Q1,
  PERCENTILE_CONT(0.5) WITHIN GROUP (
    ORDER BY
      clicks
  ) AS median,
  avg(clicks) AS mean,
  PERCENTILE_CONT(0.75) WITHIN GROUP (
    ORDER BY
      clicks
  ) AS Q3,
  max(clicks)
FROM
  tutorial.kag_conversion_data

-- 3. 광고료 기술통계량
SELECT
  min(spent),
  PERCENTILE_CONT(0.25) WITHIN GROUP (
    ORDER BY
      spent
  ) AS Q1,
  PERCENTILE_CONT(0.5) WITHIN GROUP (
    ORDER BY
      spent
  ) AS median,
  avg(spent) AS mean,
  PERCENTILE_CONT(0.75) WITHIN GROUP (
    ORDER BY
      spent
  ) AS Q3,
  max(spent)
FROM
  tutorial.kag_conversion_data

-- 4. 문의 수 기술통계량
SELECT
  min(total_conversion),
  PERCENTILE_CONT(0.25) WITHIN GROUP (
    ORDER BY
      total_conversion
  ) AS Q1,
  PERCENTILE_CONT(0.5) WITHIN GROUP (
    ORDER BY
      total_conversion
  ) AS median,
  avg(total_conversion) AS mean,
  PERCENTILE_CONT(0.75) WITHIN GROUP (
    ORDER BY
      total_conversion
  ) AS Q3,
  max(total_conversion)
FROM
  tutorial.kag_conversion_data

-- 5. 구매자 수 기술통계량
SELECT
  min(approved_conversion),
  PERCENTILE_CONT(0.25) WITHIN GROUP (
    ORDER BY
      approved_conversion
  ) AS Q1,
  PERCENTILE_CONT(0.5) WITHIN GROUP (
    ORDER BY
      approved_conversion
  ) AS median,
  avg(approved_conversion) AS mean,
  PERCENTILE_CONT(0.75) WITHIN GROUP (
    ORDER BY
      approved_conversion
  ) AS Q3,
  max(approved_conversion)
FROM
  tutorial.kag_conversion_data

-- 6. CTR 기술통계량
SELECT
  min(clicks / impressions * 100),
  PERCENTILE_CONT(0.25) WITHIN GROUP (
    ORDER BY
      clicks / impressions * 100
  ) AS Q1,
  PERCENTILE_CONT(0.5) WITHIN GROUP (
    ORDER BY
      clicks / impressions * 100
  ) AS median,
  avg(clicks / impressions * 100) AS mean,
  PERCENTILE_CONT(0.75) WITHIN GROUP (
    ORDER BY
      clicks / impressions * 100
  ) AS Q3,
  max(clicks / impressions * 100)
FROM
  tutorial.kag_conversion_data

-- 7. CVR 기술통계량
SELECT
  min(approved_conversion / clicks * 100),
  PERCENTILE_CONT(0.25) WITHIN GROUP (
    ORDER BY
      approved_conversion / clicks * 100
  ) AS Q1,
  PERCENTILE_CONT(0.5) WITHIN GROUP (
    ORDER BY
      approved_conversion / clicks * 100
  ) AS median,
  avg(approved_conversion / clicks * 100) AS mean,
  PERCENTILE_CONT(0.75) WITHIN GROUP (
    ORDER BY
      approved_conversion / clicks * 100
  ) AS Q3,
  max(approved_conversion / clicks * 100)
FROM
  (select * from tutorial.kag_conversion_data where clicks != 0) a

-- 8. CPC 기술통계량
SELECT
  min(spent / clicks),
  PERCENTILE_CONT(0.25) WITHIN GROUP (
    ORDER BY
      spent / clicks
  ) AS Q1,
  PERCENTILE_CONT(0.5) WITHIN GROUP (
    ORDER BY
      spent / clicks
  ) AS median,
  avg(spent / clicks) AS mean,
  PERCENTILE_CONT(0.75) WITHIN GROUP (
    ORDER BY
      spent / clicks
  ) AS Q3,
  max(spent / clicks)
FROM
  (select * from tutorial.kag_conversion_data where clicks != 0) a

-- 9. CPM 기술통계량
SELECT
  min(spent / impressions * 1000),
  PERCENTILE_CONT(0.25) WITHIN GROUP (
    ORDER BY
      spent / impressions * 1000
  ) AS Q1,
  PERCENTILE_CONT(0.5) WITHIN GROUP (
    ORDER BY
      spent / impressions * 1000
  ) AS median,
  avg(spent / impressions * 1000) AS mean,
  PERCENTILE_CONT(0.75) WITHIN GROUP (
    ORDER BY
      spent / impressions * 1000
  ) AS Q3,
  max(spent / impressions * 1000)
FROM
  tutorial.kag_conversion_data
