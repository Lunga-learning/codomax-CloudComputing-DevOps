output "devops_test_instance_id" {
  description = "Existing DevOps Test EC2 instance ID"
  value       = data.aws_instance.devops_test.id
}

output "devops_test_instance_type" {
  description = "Existing EC2 instance type"
  value       = data.aws_instance.devops_test.instance_type
}

output "devops_test_private_ip" {
  description = "Existing EC2 private IP address"
  value       = data.aws_instance.devops_test.private_ip
}

output "devops_test_public_ip" {
  description = "Existing EC2 public IP address"
  value       = data.aws_instance.devops_test.public_ip
}

output "devops_test_security_groups" {
  description = "Security groups attached to the existing EC2 instance"
  value       = data.aws_instance.devops_test.vpc_security_group_ids
}
