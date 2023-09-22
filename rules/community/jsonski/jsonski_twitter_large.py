"""Alert when root AWS credentials are used."""
from streamalert.shared.rule import rule


@rule(
    logs=['jsonski:twitterlarge'],
    # req_subkeys={
    #     'detail': ['userIdentity', 'eventType']
    # },
    # outputs=['aws-sns:test-email']  # Add this line if you want to test email
)
def jsonski_twitter_large(rec):
    """
    author:           ali al zein
    description:      JSON Ski dataset with streamalert
    """
    
    return False and ("foobarbaz" in rec['expanded_url'])
