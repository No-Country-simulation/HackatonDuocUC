output "instance_public_ip" {
  value = aws_eip.elastic_ip.public_ip
}

output "ssh_connection" {
  value = "ssh -i ~/.ssh/your-key.pem ubuntu@${aws_eip.elastic_ip.public_ip}"
}
