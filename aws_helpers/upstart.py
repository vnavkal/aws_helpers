from . import iam


_BATCH_PRICING_STAGING_POLICY_NAME = 'S3WriteDataExportServicer-staging'
_BATCH_PRICING_PROD_POLICY_NAME = 'S3WriteDataExportServicer'


def update_batch_pricing_staging_policy(policy_path):
    staging_policy_arn = _policy_arn(_BATCH_PRICING_STAGING_POLICY_NAME)
    return iam.update_policy(policy_path, staging_policy_arn)


def update_batch_pricing_prod_policy(policy_path):
    prod_policy_arn = _policy_arn(_BATCH_PRICING_PROD_POLICY_NAME)
    return iam.update_policy(policy_path, prod_policy_arn)


def get_batch_pricing_staging_policy_document():
    return iam.get_policy_document(_policy_arn(_BATCH_PRICING_STAGING_POLICY_NAME))


def get_batch_pricing_prod_policy_document():
    return iam.get_policy_document(_policy_arn(_BATCH_PRICING_PROD_POLICY_NAME))


def get_john_dee_staging_policy_statements():
    return iam.get_all_policy_statements_for_group('John-Dee-Staging')


def get_john_dee_production_policy_statements():
    return iam.get_all_policy_statements_for_group('John-Dee-Production')


def list_data_scientist_policies():
    return iam.list_attached_group_policies('DataScience')


def _policy_arn(policy_name):
    return f'arn:aws:iam::455849046226:policy/{policy_name}'
