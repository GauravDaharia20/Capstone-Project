import { Component, OnInit } from '@angular/core';
import { Recipe } from '../recipe.model';

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})
export class RecipeListComponent implements OnInit {

  recipes: Recipe[]=[
    new Recipe('A test Recipe','This is simple food','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWDLZ1fL_TIud_NTyYg9qcnrgMrvz4xChbIqcjLU2VJBn0nk9Us3FWl1z0b_GAqlBBj0A&usqp=CAU'),
    new Recipe('A test Recipe','This is simple food','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWDLZ1fL_TIud_NTyYg9qcnrgMrvz4xChbIqcjLU2VJBn0nk9Us3FWl1z0b_GAqlBBj0A&usqp=CAU')
  ]
  

  constructor() { }

  ngOnInit(): void {
  }

}
