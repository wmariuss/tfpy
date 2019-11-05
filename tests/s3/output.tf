output "names" {
  description = "List s3 bucket(s)'s names"
  value       = ["${module.s3.names}"]
}
