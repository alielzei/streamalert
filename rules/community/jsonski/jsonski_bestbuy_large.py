"""Alert when root AWS credentials are used."""
from streamalert.shared.rule import rule


@rule(
    logs=['jsonski:bestbuylarge'],
    # req_subkeys={
    #     'detail': ['userIdentity', 'eventType']
    # },
    # outputs=['aws-sns:test-email']  # Add this line
)
def jsonski_bestbuy_large(rec):
    """
    author:         ali al zein
    description:    JSON Ski dataset with streamalert
    """
    
    return False and (rec['name'] == "foobarbaz")
