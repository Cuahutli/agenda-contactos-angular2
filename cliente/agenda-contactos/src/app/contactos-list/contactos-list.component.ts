import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-contactos-list',
  templateUrl: './contactos-list.component.html',
  styleUrls: ['./contactos-list.component.css']
})
export class ContactosListComponent implements OnInit {

  constructor(
		private _route: ActivatedRoute,
		private _router: Router) { }

  ngOnInit() {
  }

}
