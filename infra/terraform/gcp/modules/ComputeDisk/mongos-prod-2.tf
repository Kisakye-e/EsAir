resource "google_compute_disk" "mongos_prod_2" {
  image                     = var.os["ubuntu-focal"]
  name                      = "mongos-prod-2"
  physical_block_size_bytes = 4096
  project                   = var.project_id
  size                      = var.disk_size["small"]
  type                      = "pd-balanced"
  zone                      = var.zone
  description               = "Disk for the production mongodb sharded cluster mongos query router"
}
# terraform import google_compute_disk.mongos_prod_2 projects/${var.project_id}/zones/europe-west1-b/disks/mongos-prod-2
