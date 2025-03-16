resource "aws_ecs_service" "backend_service" {
  name            = "portfolio-backend-service"
  cluster         = aws_ecs_cluster.portfolio_cluster.id
  task_definition = aws_ecs_task_definition.backend_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = ["subnet-12345678", "subnet-23456789"]
    security_groups = ["sg-12345678"] 
  }
}

resource "aws_ecs_service" "frontend_service" {
  name            = "portfolio-frontend-service"
  cluster         = aws_ecs_cluster.portfolio_cluster.id
  task_definition = aws_ecs_task_definition.frontend_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = ["subnet-12345678", "subnet-23456789"]
    security_groups = ["sg-12345678"]
  }
}
