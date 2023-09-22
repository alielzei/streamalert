"""Alert when root AWS credentials are used."""
from streamalert.shared.rule import rule


@rule(
    logs=['jsonski:twittersmall'],
    # req_subkeys={
    #     'detail': ['userIdentity', 'eventType']
    # },
    # outputs=['aws-sns:test-email']  # Add this line
)
def jsonski_twitter_small(rec):
    """
    author:           ali al zein
    description:      JSON Ski dataset with streamalert
    """
    
    return False and ("foobarbaz" in rec['expanded_url'])
