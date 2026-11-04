data "aws_instance" "devops_test" {
  filter {
    name   = "instance-id"
    values = ["i-067fed8cab43520dd"]
  }
}
