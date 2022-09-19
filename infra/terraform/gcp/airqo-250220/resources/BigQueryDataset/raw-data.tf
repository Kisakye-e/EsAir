resource "google_bigquery_dataset" "raw_data" {
  access {
    role          = "OWNER"
    special_group = "projectOwners"
  }

  access {
    role          = "READER"
    special_group = "projectReaders"
  }

  access {
    role          = "WRITER"
    special_group = "projectWriters"
  }

  dataset_id                 = "raw_data"
  delete_contents_on_destroy = false
  location                   = "EU"
  project                    = "airqo-250220"
}
# terraform import google_bigquery_dataset.raw_data projects/airqo-250220/datasets/raw_data
