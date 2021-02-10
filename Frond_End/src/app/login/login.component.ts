/**
 * Created by xavi on 5/16/17.
 */
import {Component, OnInit} from "@angular/core";
import {Validators, FormGroup, FormBuilder} from "@angular/forms";
import {LoginObject} from "./shared/login-object.model";
import {Login} from "./shared/login.model";
import {AuthenticationService} from "./shared/authentication.service";
import {StorageService} from "../core/services/storage.service";
import {Router} from "@angular/router";


@Component({
  selector: 'login',
  templateUrl: 'login.component.html'
})

export class LoginComponent implements OnInit {
  public loginForm: FormGroup;
  public submitted: Boolean = false;
  public error: {code: number, message: string} = null;
  some: any;
  user: boolean;
  password: boolean;
  constructor(private formBuilder: FormBuilder,
              private authenticationService: AuthenticationService,
              private storageService: StorageService,
              private router: Router) { }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    })
  }

  public submitLogin(): void {
    this.submitted = true;
    this.error = null;
    if(this.loginForm.valid){
      this.authenticationService.login(new Login(this.loginForm.value)).subscribe(
        data => this.correctLogin(data)
      )
    }
  }
  private correctLogin(data: any){
    if(data=='Incorrect password' ||data=='Incorrect user'){
      this.user=true;
    }else{
      this.user=false;
    }
    this.storageService.setCurrentSession(data);
    this.router.navigate(['/home']);
  }

}
