resource "aws_ecs_task_definition" "backend_task" {
  family                   = "portfolio-backend-task"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  network_mode             = "awsvpc"

  container_definitions = jsonencode([
    {
      name      = "portfolio-backend"
      image     = "${aws_ecr_repository.backend_repo.repository_url}:latest"
      cpu       = 256
      memory    = 512
      essential = true
      portMappings = [{ containerPort = 5000 }]
    }
  ])
}

resource "aws_ecs_task_definition" "frontend_task" {
  family                   = "portfolio-frontend-task"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  network_mode             = "awsvpc"

  container_definitions = jsonencode([
    {
      name      = "portfolio-frontend"
      image     = "${aws_ecr_repository.frontend_repo.repository_url}:latest"
      cpu       = 256
      memory    = 512
      essential = true
      portMappings = [{ containerPort = 80 }]
    }
  ])
}
