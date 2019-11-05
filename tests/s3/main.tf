module "s3" {
  source = ""

  region        = "us-east-2"
  names         = ["terraformpy-bucket", "terraformpy"]
  enable        = true
  force_destroy = true
}
