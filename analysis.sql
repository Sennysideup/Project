-- 타겟팅 옵션별 CTR & CVR 비교
-- 1. 타게팅 옵션이 잘못 설정된 경우
-- 광고별 CTR이 타겟팅 옵션의 전체 평균 CTR보다 높고, 광고별 CVR이 타겟팅 옵션의 전체 평균 CVR보다 낮음
SELECT
  b.gender,
  b.age,
  sum(b.cnt_per_id) AS need_retarget,
  avg(d.cnt_per_target) AS total_cnt,
  sum(b.cnt_per_id) / avg(d.cnt_per_target) * 100 AS ratio
FROM
  (
    SELECT
      fb_campaign_id,
      gender,
      age,
      avg(clicks / impressions * 100) AS CTR,
      avg(approved_conversion / clicks * 100) AS CVR,
      count(DISTINCT fb_campaign_id) AS cnt_per_id
    FROM
      (
        SELECT
          *
        FROM
          tutorial.kag_conversion_data
        WHERE
          clicks != 0
      ) a
    GROUP BY
      fb_campaign_id,
      gender,
      age
  ) b
  INNER JOIN (
    SELECT
      gender,
      age,
      avg(clicks / impressions * 100) AS CTR,
      avg(approved_conversion / clicks * 100) AS CVR,
      count(DISTINCT fb_campaign_id) AS cnt_per_target
    FROM
      (
        SELECT
          *
        FROM
          tutorial.kag_conversion_data
        WHERE
          clicks != 0
      ) c
    GROUP BY
      gender,
      age
  ) d ON b.gender = d.gender
  AND b.age = d.age
  AND b.CTR > d.CTR
  AND b.CVR < d.CVR
GROUP BY
  b.gender,
  b.age

-- 2. 광고의 매력도가 떨어지는 경우
-- 광고별 CTR이 타겟팅 옵션의 전체 평균 CTR보다 낮고, 광고별 CVR이 타겟팅 옵션의 전체 평균 CVR보다 높음
SELECT
  b.gender,
  b.age,
  sum(b.cnt_per_id) AS need_replace_image,
  avg(d.cnt_per_target) AS total_cnt,
  sum(b.cnt_per_id) / avg(d.cnt_per_target) * 100 AS ratio
FROM
  (
    SELECT
      fb_campaign_id,
      gender,
      age,
      avg(clicks / impressions * 100) AS CTR,
      avg(approved_conversion / clicks * 100) AS CVR,
      count(DISTINCT fb_campaign_id) AS cnt_per_id
    FROM
      (
        SELECT
          *
        FROM
          tutorial.kag_conversion_data
        WHERE
          clicks != 0
      ) a
    GROUP BY
      fb_campaign_id,
      gender,
      age
  ) b
  INNER JOIN (
    SELECT
      gender,
      age,
      avg(clicks / impressions * 100) AS CTR,
      avg(approved_conversion / clicks * 100) AS CVR,
      count(DISTINCT fb_campaign_id) AS cnt_per_target
    FROM
      (
        SELECT
          *
        FROM
          tutorial.kag_conversion_data
        WHERE
          clicks != 0
      ) c
    GROUP BY
      gender,
      age
  ) d ON b.gender = d.gender
  AND b.age = d.age
  AND b.CTR < d.CTR
  AND b.CVR > d.CVR
GROUP BY
  b.gender,
  b.age

-- 타겟팅 옵션별 광고 비용 비교
-- 1. 광고별 CPM이 타겟팅 옵션의 전체 평균 CPM보다 높은 경우
SELECT
  b.gender,
  b.age,
  sum(b.cnt_per_id) AS need_extend_target,
  avg(d.cnt_per_target) AS total_cnt,
  sum(b.cnt_per_id) / avg(d.cnt_per_target) * 100 AS ratio
FROM
  (
    SELECT
      fb_campaign_id,
      gender,
      age,
      avg(spent / impressions * 100) AS CPM,
      count(DISTINCT fb_campaign_id) AS cnt_per_id
    FROM
      (
        SELECT
          *
        FROM
          tutorial.kag_conversion_data
        WHERE
          clicks != 0
      ) a
    GROUP BY
      fb_campaign_id,
      gender,
      age
  ) b
  INNER JOIN (
    SELECT
      gender,
      age,
      avg(spent / impressions * 100) AS CPM,
      count(DISTINCT fb_campaign_id) AS cnt_per_target
    FROM
      (
        SELECT
          *
        FROM
          tutorial.kag_conversion_data
        WHERE
          clicks != 0
      ) c
    GROUP BY
      gender,
      age
  ) d ON b.gender = d.gender
  AND b.age = d.age
  AND b.CPM > d.CPM
GROUP BY
  b.gender,
  b.age

-- 2 광고별 CPC가 타겟팅 옵션의 전체 평균 CPC보다 높은 경우
SELECT
  b.gender,
  b.age,
  sum(b.cnt_per_id) AS need_replace_image,
  avg(d.cnt_per_target) AS total_cnt,
  sum(b.cnt_per_id) / avg(d.cnt_per_target) * 100 AS ratio
FROM
  (
    SELECT
      fb_campaign_id,
      gender,
      age,
      avg(spent / clicks) AS CPC,
      count(DISTINCT fb_campaign_id) AS cnt_per_id
    FROM
      (
        SELECT
          *
        FROM
          tutorial.kag_conversion_data
        WHERE
          clicks != 0
      ) a
    GROUP BY
      fb_campaign_id,
      gender,
      age
  ) b
  INNER JOIN (
    SELECT
      gender,
      age,
      avg(spent / clicks) AS CPC,
      count(DISTINCT fb_campaign_id) AS cnt_per_target
    FROM
      (
        SELECT
          *
        FROM
          tutorial.kag_conversion_data
        WHERE
          clicks != 0
      ) c
    GROUP BY
      gender,
      age
  ) d ON b.gender = d.gender
  AND b.age = d.age
  AND b.CPC > d.CPC
GROUP BY
  b.gender,
  b.age
