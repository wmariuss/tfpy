module "ec2" {
  source = ""

  number_of_instances = 2

  name   = "terraformpy-test"
  region = "us-east-2"

  instance_type = "t2.small"
  ssh_key_name  = "122949715051-us-east-2"
  vpc_id        = "vpc-05657b3cc7db78b6f"
  subnet        = "subnet-04f4d91472f483b7a"
  user_data     = "setup.sh"

  associate_public_ip_address = false
  enable_elastic_ip           = false

  tags = {
    Owner       = "Marius Stanca"
    Environment = "testing"
    Name        = "terraformpy"
  }

  volume_tags = {
    Owner      = "Marius Stanca"
    created_by = "terraform"
    Name       = "terraformpy"
  }
}
