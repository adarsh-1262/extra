from flask_restful import Api,Resource,reqparse
from .models import *
api=Api()

 #parser for Campaign
c_parser=reqparse.RequestParser()
c_parser.add_argument("c_name")
c_parser.add_argument("description")
c_parser.add_argument("budget")
c_parser.add_argument("start_date")
c_parser.add_argument("end_date")
c_parser.add_argument("goal")
c_parser.add_argument("niche")


class CampaignApi(Resource):

    def get(self,sponser_id):
        campaigns=Campaign.query.filter_by(sponser_id=sponser_id).all()
        sponser_campaigns=[]
        for campaign in campaigns:
            campaign_details={}
            campaign_details['id']=campaign.id
            campaign_details['c_name']=campaign.c_name
            campaign_details['visibility']=campaign.visibility
            campaign_details['description']=campaign.description
            campaign_details['budget']=campaign.budget
            campaign_details['start_date']=campaign.start_date
            campaign_details['end_date']=campaign.end_date
            campaign_details['campaign_status']=campaign.campaign_status
            campaign_details['campaign_flagged_status']=campaign.campaign_flagged_status
            campaign_details['no_of_ads']=campaign.no_of_ads
            campaign_details['progress']=campaign.progress
            campaign_details['goal']=campaign.goal
            campaign_details['sponser_id']=campaign.sponser_id
            campaign_details['niche']=campaign.niche
            sponser_campaigns.append(campaign_details)
        return sponser_campaigns
    
    def post(self,sponser_id):
        pass

    def put(self,campaign_id):
        pass

    def delete(self,campaign_id):
        pass



api.add_resource(CampaignApi,"/api/campaigns/<int:sponser_id>")