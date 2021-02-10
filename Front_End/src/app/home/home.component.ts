/**
 * Created by xavi on 5/16/17.
 */
import {Component, OnInit} from "@angular/core";
import {StorageService} from "../core/services/storage.service";
import {User} from "../core/models/user.model";
import {AuthenticationService} from "../login/shared/authentication.service";
@Component({
  selector: 'home',
  templateUrl: 'home.component.html'
})

export class HomeComponent implements OnInit {

  constructor(
    private storageService: StorageService,
    private authenticationService: AuthenticationService
  ) { }

  ngOnInit() {
    
  }

  public logout(): void{
    this.storageService.logout();
  }

}
