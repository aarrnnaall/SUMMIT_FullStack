import {Injectable} from "@angular/core";
import { Router } from '@angular/router';
import jwt_decode from 'jwt-decode';
@Injectable()
export class StorageService {

  private localStorageService;
  private currentSession : any;
  some: any=null;
  token: any;
  constructor(private router: Router) {
    this.localStorageService = localStorage;
    this.currentSession = this.loadSessionData();
  }

  setCurrentSession(session: any): void {
    this.token=session;
    try{
      this.some=jwt_decode(this.token.jwt_token);
      this.localStorageService.setItem('currentUser', JSON.stringify(session));
    }
    catch{
      this.some=null;
    }
  }

  loadSessionData(): any{
    var sessionStr = this.localStorageService.getItem('currentUser');
    return (sessionStr) ? <any> JSON.parse(sessionStr) : null;
  }

  getCurrentSession(): any {
    
    return this.some;
  }

  removeCurrentSession(): void {
    this.localStorageService.removeItem('currentUser');
    this.currentSession = null;
  }

  isAuthenticated(): boolean {
    return (this.getCurrentToken() != null) ? true : false;
  };

  getCurrentToken(): string {
    try{
    var session = this.getCurrentSession();

    if (session.some!="thissecret"){
      return null;
    }else{
      return session;
    }
  }catch{
    return null;
  }
  };

  logout(): void{
    this.removeCurrentSession();
    this.router.navigate(['/login']);
  }

}
