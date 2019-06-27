from magine.enrichment.enrichr import run_enrichment_for_project
from exp_data import exp_data


if __name__ == '__main__':
    run_enrichment_for_project(exp_data, 'bendamustine')