resource "google_bigquery_dataset" "channel" {
  access {
    role          = "OWNER"
    user_by_email = "g-ranked-reverend@fivetran-production.iam.gserviceaccount.com"
  }

  access {
    role          = "READER"
    special_group = "projectOwners"
  }

  access {
    role          = "READER"
    special_group = "projectWriters"
  }

  dataset_id                 = "channel"
  delete_contents_on_destroy = false
  location                   = "europe-west6"
  project                    = "airqo-250220"
}
# terraform import google_bigquery_dataset.channel projects/airqo-250220/datasets/channel
