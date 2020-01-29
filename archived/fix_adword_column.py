


def extract_col(sql_line):
    start = 'V:'
    end = '::'
    s = sql_line
    return   (s[s.find(start)+len(start):s.rfind(end)])
    #print (s[s.find(start)+len(start):s.rfind(end)])

# EnhancedDisplayCreativeLandscapeLogoImageMediaId -> ENHANCED_DISPLAY_CREATIVE_LANDSCAPE_LOGO_IMAGE_MEDIA_ID
def fix_dbt_col(col_name):
    import re 
    result = re.sub('(?<=[A-Za-z])(?=[A-Z][a-z])', '~', col_name,)
    result = re.split('~', result)
    return '_'.join(result).upper()
    

# -------------------------------  DEMO -------------------------------

# for line in sql.splitlines():
#     if 'V' not in line:
#         print (line)
#     else:
#         print ( line.split(' as ')[0]  +  " as " +  fix_dbt_col(extract_col(line)) + ',')
        
  
# output :  
      
# SELECT
# '846_445_0947' AS "ACCOUNT_ID",
#  V:"AdGroupId"::INTEGER as "AD_GROUP_ID",
#  V:"BiddingStrategyId"::INTEGER as "BIDDING_STRATEGY_ID",
#  V:"CampaignId"::INTEGER as "CAMPAIGN_ID",
#  V:"CpcBid"::VARCHAR as "CPC_BID",
#  V:"CpvBid"::VARCHAR as "CPV_BID",
#  V:"ExternalCustomerId"::INTEGER as "EXTERNAL_CUSTOMER_ID",
#  V:"AdGroupDesktopBidModifier"::FLOAT as "AD_GROUP_DESKTOP_BID_MODIFIER",
#  V:"AdGroupMobileBidModifier"::FLOAT as "AD_GROUP_MOBILE_BID_MODIFIER",
#  V:"AdGroupName"::VARCHAR as "AD_GROUP_NAME",
#  V:"AdGroupStatus"::VARCHAR as "AD_GROUP_STATUS",
#  V:"AdGroupTabletBidModifier"::FLOAT as "AD_GROUP_TABLET_BID_MODIFIER",
#  V:"AdGroupType"::VARCHAR as "AD_GROUP_TYPE",
#  V:"AdRotationMode"::VARCHAR as "AD_ROTATION_MODE",
#  V:"BiddingStrategyName"::VARCHAR as "BIDDING_STRATEGY_NAME",
#  V:"BiddingStrategySource"::VARCHAR as "BIDDING_STRATEGY_SOURCE",
#  V:"BiddingStrategyType"::VARCHAR as "BIDDING_STRATEGY_TYPE",
#  V:"ContentBidCriterionTypeGroup"::VARCHAR as "CONTENT_BID_CRITERION_TYPE_GROUP",
#  V:"CpmBidStr"::VARCHAR as "CPM_BID_STR",
#  V:"EffectiveTargetRoas"::FLOAT as "EFFECTIVE_TARGET_ROAS",
#  V:"EffectiveTargetRoasSource"::VARCHAR as "EFFECTIVE_TARGET_ROAS_SOURCE",
#  V:"EnhancedCpcEnabled"::BOOLEAN as "ENHANCED_CPC_ENABLED",
#  V:"LabelIds"::VARCHAR as "LABEL_IDS",
#  V:"Labels"::VARCHAR as "LABELS",
#  V:"TargetCpa"::INTEGER as "TARGET_CPA",
#  V:"TargetCpaBidSource"::VARCHAR as "TARGET_CPA_BID_SOURCE",
#  V:"TrackingUrlTemplate"::VARCHAR as "TRACKING_URL_TEMPLATE",
#  V:"UrlCustomParameters"::VARCHAR as "URL_CUSTOM_PARAMETERS",
# FROM "STAGING"."ADWORDS_P_ADGROUP_846_445_0947"

# UNION ALL

# SELECT
# '336_727_9774' AS "ACCOUNT_ID",
#  V:"AdGroupId"::INTEGER as "AD_GROUP_ID",
#  V:"BiddingStrategyId"::INTEGER as "BIDDING_STRATEGY_ID",
#  V:"CampaignId"::INTEGER as "CAMPAIGN_ID",
#  V:"CpcBid"::VARCHAR as "CPC_BID",
#  V:"CpvBid"::VARCHAR as "CPV_BID",
#  V:"ExternalCustomerId"::INTEGER as "EXTERNAL_CUSTOMER_ID",
#  V:"AdGroupDesktopBidModifier"::FLOAT as "AD_GROUP_DESKTOP_BID_MODIFIER",
#  V:"AdGroupMobileBidModifier"::FLOAT as "AD_GROUP_MOBILE_BID_MODIFIER",
#  V:"AdGroupName"::VARCHAR as "AD_GROUP_NAME",
#  V:"AdGroupStatus"::VARCHAR as "AD_GROUP_STATUS",
#  V:"AdGroupTabletBidModifier"::FLOAT as "AD_GROUP_TABLET_BID_MODIFIER",
#  V:"AdGroupType"::VARCHAR as "AD_GROUP_TYPE",
#  V:"AdRotationMode"::VARCHAR as "AD_ROTATION_MODE",
#  V:"BiddingStrategyName"::VARCHAR as "BIDDING_STRATEGY_NAME",
#  V:"BiddingStrategySource"::VARCHAR as "BIDDING_STRATEGY_SOURCE",
#  V:"BiddingStrategyType"::VARCHAR as "BIDDING_STRATEGY_TYPE",
#  V:"ContentBidCriterionTypeGroup"::VARCHAR as "CONTENT_BID_CRITERION_TYPE_GROUP",
#  V:"CpmBidStr"::VARCHAR as "CPM_BID_STR",
#  V:"EffectiveTargetRoas"::FLOAT as "EFFECTIVE_TARGET_ROAS",
#  V:"EffectiveTargetRoasSource"::VARCHAR as "EFFECTIVE_TARGET_ROAS_SOURCE",
#  V:"EnhancedCpcEnabled"::BOOLEAN as "ENHANCED_CPC_ENABLED",
#  V:"LabelIds"::VARCHAR as "LABEL_IDS",
#  V:"Labels"::VARCHAR as "LABELS",
#  V:"TargetCpa"::INTEGER as "TARGET_CPA",
#  V:"TargetCpaBidSource"::VARCHAR as "TARGET_CPA_BID_SOURCE",
#  V:"TrackingUrlTemplate"::VARCHAR as "TRACKING_URL_TEMPLATE",
#  V:"UrlCustomParameters"::VARCHAR as "URL_CUSTOM_PARAMETERS",
# FROM "STAGING"."ADWORDS_P_ADGROUP_336_727_9774"

# UNION ALL

# SELECT
# '894_635_1017' AS "ACCOUNT_ID",
#  V:"AdGroupId"::INTEGER as "AD_GROUP_ID",
#  V:"BiddingStrategyId"::INTEGER as "BIDDING_STRATEGY_ID",
#  V:"CampaignId"::INTEGER as "CAMPAIGN_ID",
#  V:"CpcBid"::VARCHAR as "CPC_BID",
#  V:"CpvBid"::VARCHAR as "CPV_BID",
#  V:"ExternalCustomerId"::INTEGER as "EXTERNAL_CUSTOMER_ID",
#  V:"AdGroupDesktopBidModifier"::FLOAT as "AD_GROUP_DESKTOP_BID_MODIFIER",
#  V:"AdGroupMobileBidModifier"::FLOAT as "AD_GROUP_MOBILE_BID_MODIFIER",
#  V:"AdGroupName"::VARCHAR as "AD_GROUP_NAME",
#  V:"AdGroupStatus"::VARCHAR as "AD_GROUP_STATUS",
#  V:"AdGroupTabletBidModifier"::FLOAT as "AD_GROUP_TABLET_BID_MODIFIER",
#  V:"AdGroupType"::VARCHAR as "AD_GROUP_TYPE",
#  V:"AdRotationMode"::VARCHAR as "AD_ROTATION_MODE",
#  V:"BiddingStrategyName"::VARCHAR as "BIDDING_STRATEGY_NAME",
#  V:"BiddingStrategySource"::VARCHAR as "BIDDING_STRATEGY_SOURCE",
#  V:"BiddingStrategyType"::VARCHAR as "BIDDING_STRATEGY_TYPE",
#  V:"ContentBidCriterionTypeGroup"::VARCHAR as "CONTENT_BID_CRITERION_TYPE_GROUP",
#  V:"CpmBidStr"::VARCHAR as "CPM_BID_STR",
#  V:"EffectiveTargetRoas"::FLOAT as "EFFECTIVE_TARGET_ROAS",
#  V:"EffectiveTargetRoasSource"::VARCHAR as "EFFECTIVE_TARGET_ROAS_SOURCE",
#  V:"EnhancedCpcEnabled"::BOOLEAN as "ENHANCED_CPC_ENABLED",
#  V:"LabelIds"::VARCHAR as "LABEL_IDS",
#  V:"Labels"::VARCHAR as "LABELS",
#  V:"TargetCpa"::INTEGER as "TARGET_CPA",
#  V:"TargetCpaBidSource"::VARCHAR as "TARGET_CPA_BID_SOURCE",
#  V:"TrackingUrlTemplate"::VARCHAR as "TRACKING_URL_TEMPLATE",
#  V:"UrlCustomParameters"::VARCHAR as "URL_CUSTOM_PARAMETERS",
# FROM "STAGING"."ADWORDS_P_ADGROUP_894_635_1017"






# sql = """

# SELECT
# '846_445_0947' AS "ACCOUNT_ID",
#  V:"AdGroupId"::INTEGER as "AdGroupId" ,
#  V:"BiddingStrategyId"::INTEGER as "BiddingStrategyId" ,
#  V:"CampaignId"::INTEGER as "CampaignId" ,
#  V:"CpcBid"::VARCHAR as "CpcBid" ,
#  V:"CpvBid"::VARCHAR as "CpvBid" ,
#  V:"ExternalCustomerId"::INTEGER as "ExternalCustomerId" ,
#  V:"AdGroupDesktopBidModifier"::FLOAT as "AdGroupDesktopBidModifier" ,
#  V:"AdGroupMobileBidModifier"::FLOAT as "AdGroupMobileBidModifier" ,
#  V:"AdGroupName"::VARCHAR as "AdGroupName" ,
#  V:"AdGroupStatus"::VARCHAR as "AdGroupStatus" ,
#  V:"AdGroupTabletBidModifier"::FLOAT as "AdGroupTabletBidModifier" ,
#  V:"AdGroupType"::VARCHAR as "AdGroupType" ,
#  V:"AdRotationMode"::VARCHAR as "AdRotationMode" ,
#  V:"BiddingStrategyName"::VARCHAR as "BiddingStrategyName" ,
#  V:"BiddingStrategySource"::VARCHAR as "BiddingStrategySource" ,
#  V:"BiddingStrategyType"::VARCHAR as "BiddingStrategyType" ,
#  V:"ContentBidCriterionTypeGroup"::VARCHAR as "ContentBidCriterionTypeGroup" ,
#  V:"CpmBidStr"::VARCHAR as "CpmBidStr" ,
#  V:"EffectiveTargetRoas"::FLOAT as "EffectiveTargetRoas" ,
#  V:"EffectiveTargetRoasSource"::VARCHAR as "EffectiveTargetRoasSource" ,
#  V:"EnhancedCpcEnabled"::BOOLEAN as "EnhancedCpcEnabled" ,
#  V:"LabelIds"::VARCHAR as "LabelIds" ,
#  V:"Labels"::VARCHAR as "Labels" ,
#  V:"TargetCpa"::INTEGER as "TargetCpa" ,
#  V:"TargetCpaBidSource"::VARCHAR as "TargetCpaBidSource" ,
#  V:"TrackingUrlTemplate"::VARCHAR as "TrackingUrlTemplate" ,
#  V:"UrlCustomParameters"::VARCHAR as "UrlCustomParameters"
# FROM "STAGING"."ADWORDS_P_ADGROUP_846_445_0947"

# UNION ALL

# SELECT
# '336_727_9774' AS "ACCOUNT_ID",
#  V:"AdGroupId"::INTEGER as "AdGroupId" ,
#  V:"BiddingStrategyId"::INTEGER as "BiddingStrategyId" ,
#  V:"CampaignId"::INTEGER as "CampaignId" ,
#  V:"CpcBid"::VARCHAR as "CpcBid" ,
#  V:"CpvBid"::VARCHAR as "CpvBid" ,
#  V:"ExternalCustomerId"::INTEGER as "ExternalCustomerId" ,
#  V:"AdGroupDesktopBidModifier"::FLOAT as "AdGroupDesktopBidModifier" ,
#  V:"AdGroupMobileBidModifier"::FLOAT as "AdGroupMobileBidModifier" ,
#  V:"AdGroupName"::VARCHAR as "AdGroupName" ,
#  V:"AdGroupStatus"::VARCHAR as "AdGroupStatus" ,
#  V:"AdGroupTabletBidModifier"::FLOAT as "AdGroupTabletBidModifier" ,
#  V:"AdGroupType"::VARCHAR as "AdGroupType" ,
#  V:"AdRotationMode"::VARCHAR as "AdRotationMode" ,
#  V:"BiddingStrategyName"::VARCHAR as "BiddingStrategyName" ,
#  V:"BiddingStrategySource"::VARCHAR as "BiddingStrategySource" ,
#  V:"BiddingStrategyType"::VARCHAR as "BiddingStrategyType" ,
#  V:"ContentBidCriterionTypeGroup"::VARCHAR as "ContentBidCriterionTypeGroup" ,
#  V:"CpmBidStr"::VARCHAR as "CpmBidStr" ,
#  V:"EffectiveTargetRoas"::FLOAT as "EffectiveTargetRoas" ,
#  V:"EffectiveTargetRoasSource"::VARCHAR as "EffectiveTargetRoasSource" ,
#  V:"EnhancedCpcEnabled"::BOOLEAN as "EnhancedCpcEnabled" ,
#  V:"LabelIds"::VARCHAR as "LabelIds" ,
#  V:"Labels"::VARCHAR as "Labels" ,
#  V:"TargetCpa"::INTEGER as "TargetCpa" ,
#  V:"TargetCpaBidSource"::VARCHAR as "TargetCpaBidSource" ,
#  V:"TrackingUrlTemplate"::VARCHAR as "TrackingUrlTemplate" ,
#  V:"UrlCustomParameters"::VARCHAR as "UrlCustomParameters"
# FROM "STAGING"."ADWORDS_P_ADGROUP_336_727_9774"

# UNION ALL

# SELECT
# '894_635_1017' AS "ACCOUNT_ID",
#  V:"AdGroupId"::INTEGER as "AdGroupId" ,
#  V:"BiddingStrategyId"::INTEGER as "BiddingStrategyId" ,
#  V:"CampaignId"::INTEGER as "CampaignId" ,
#  V:"CpcBid"::VARCHAR as "CpcBid" ,
#  V:"CpvBid"::VARCHAR as "CpvBid" ,
#  V:"ExternalCustomerId"::INTEGER as "ExternalCustomerId" ,
#  V:"AdGroupDesktopBidModifier"::FLOAT as "AdGroupDesktopBidModifier" ,
#  V:"AdGroupMobileBidModifier"::FLOAT as "AdGroupMobileBidModifier" ,
#  V:"AdGroupName"::VARCHAR as "AdGroupName" ,
#  V:"AdGroupStatus"::VARCHAR as "AdGroupStatus" ,
#  V:"AdGroupTabletBidModifier"::FLOAT as "AdGroupTabletBidModifier" ,
#  V:"AdGroupType"::VARCHAR as "AdGroupType" ,
#  V:"AdRotationMode"::VARCHAR as "AdRotationMode" ,
#  V:"BiddingStrategyName"::VARCHAR as "BiddingStrategyName" ,
#  V:"BiddingStrategySource"::VARCHAR as "BiddingStrategySource" ,
#  V:"BiddingStrategyType"::VARCHAR as "BiddingStrategyType" ,
#  V:"ContentBidCriterionTypeGroup"::VARCHAR as "ContentBidCriterionTypeGroup" ,
#  V:"CpmBidStr"::VARCHAR as "CpmBidStr" ,
#  V:"EffectiveTargetRoas"::FLOAT as "EffectiveTargetRoas" ,
#  V:"EffectiveTargetRoasSource"::VARCHAR as "EffectiveTargetRoasSource" ,
#  V:"EnhancedCpcEnabled"::BOOLEAN as "EnhancedCpcEnabled" ,
#  V:"LabelIds"::VARCHAR as "LabelIds" ,
#  V:"Labels"::VARCHAR as "Labels" ,
#  V:"TargetCpa"::INTEGER as "TargetCpa" ,
#  V:"TargetCpaBidSource"::VARCHAR as "TargetCpaBidSource" ,
#  V:"TrackingUrlTemplate"::VARCHAR as "TrackingUrlTemplate" ,
#  V:"UrlCustomParameters"::VARCHAR as "UrlCustomParameters" 
# FROM "STAGING"."ADWORDS_P_ADGROUP_894_635_1017"

# """