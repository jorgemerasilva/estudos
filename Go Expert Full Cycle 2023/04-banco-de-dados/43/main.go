package main

import (
	"fmt"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

type Product struct {
	ID    int `gorm:"primaryKey"`
	Name  string
	Price float64
	gorm.Model
}

func main() {
	dsn := "root:root@tcp(localhost:3306)/goexpert"
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		panic(err)
	}

	db.AutoMigrate(&Product{})

	//create
	db.Create(&Product{
		Name:  "Notebook",
		Price: 1000.0,
	})

	//create batch
	products := []Product{
		{Name: "Notebook", Price: 1000.00},
		{Name: "Iphone 10", Price: 1000.00},
		{Name: "Galaxy", Price: 1000.00},
		{Name: "xaiomi", Price: 1000.00},
	}

	db.Create(&products)

	//select one
	var product Product
	db.First(&product, 1)
	fmt.Println(product)

	db.First(&product, "name = ?", "Notebook")
	fmt.Println(product)

	//select all
	var products01 []Product
	db.Find(&products01)
	for _, product := range products01 {
		fmt.Println(product)
	}

	//Limit e offset
	var products02 []Product
	db.Limit(2).Offset(2).Find(&products02)
	for _, product := range products02 {
		fmt.Println(product)
	}

	//where
	//select all
	var products03 []Product
	db.Where("price > ?", 100).Find(&products03)
	for _, product := range products03 {
		fmt.Println(product)
	}

	//alterar algo do produto
	var p Product
	db.First(&p, 1)
	p.Name = "Lanterna"
	db.Save(&p)

	//Deletar
	var p2 Product
	db.First(&p2, 1)
	db.Delete(&p2)

}
