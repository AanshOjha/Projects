terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
  }
}
# provide credentials 
provider "azurerm" {
  subscription_id = "XXXXXXXXXXXXXXxxx"
  client_id       = "XXXXXXXXXXXXxxxxx"
  client_secret   = "5XXXXXXXXXXXXXXXXXxx"
  tenant_id       = "XXXXXXXXXXXXXXXXXXXXXXx"
  features {}
}
