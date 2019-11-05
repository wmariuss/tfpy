output "ec2_instance_id" {
  value = "${module.ec2.ec2_instance_id}"
}

output "public_ip_address" {
  value = "${module.ec2.public_ip_address}"
}

output "private_ip_address" {
  value = "${module.ec2.private_ip_address}"
}

output "ec2_instance_name" {
  value = "${module.ec2.ec2_instance_name}"
}
