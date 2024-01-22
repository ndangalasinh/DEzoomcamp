variable "credentials" {
  description = "my gcp credentials"
  default     = "./funguo/terraform-411819-fc115d16b7d4.json"

}
variable "bq_dataset_name" {
  description = "my dataset for big query"
  default     = "demo_dataset"

}
variable "project" {
  description = "project name"
  default     = "terraform-411819"

}
variable "gcs_storage_bucket_name" {
  description = "gcs bucket name"
  default     = "ndangalasibucket"

}
variable "gcs_storage_class" {
  description = "gcs bucket class"
  default     = "STANDARD"

}
variable "location" {
  description = "project location "
  default     = "US"

}

variable "region" {
  description = "project region"
  default     = "us-central1"

}