terraform {
  required_providers {
    github = {
      source = "integrations/github"
      version = "5.7.0"
    }
  }
}

provider "github" {
  token = "XXXXXXXXXXXXXXXXXXXXXXXXX1"
}

resource "github_repository" "example" {
  name        = "terraform-Learning"
  description = "This repository was created by using Github provider of terraform"

  visibility  = "public"

}
