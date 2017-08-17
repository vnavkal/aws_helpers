from . import iam


def get_batch_pricing_staging_policy_document():
    arn = 'arn:aws:iam::455849046226:policy/S3WriteDataExportServicer-staging'
    return iam.get_policy_document(arn)


def get_batch_pricing_production_policy_document():
    arn = 'arn:aws:iam::455849046226:policy/S3WriteDataExportServicer'
    return iam.get_policy_document(arn)


def get_john_dee_staging_policy_statements():
    return iam.get_all_policy_statements_for_group('John-Dee-Staging')


def get_john_dee_production_policy_statements():
    return iam.get_all_policy_statements_for_group('John-Dee-Production')


def list_data_scientist_policies():
    return iam.list_attached_group_policies('DataScience')
