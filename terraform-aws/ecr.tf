resource "aws_ecr_repository" "backend_repo" {
  name = "portfolio-backend"
}

resource "aws_ecr_repository" "frontend_repo" {
  name = "portfolio-frontend"
}
