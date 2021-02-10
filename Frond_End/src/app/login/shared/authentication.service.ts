import {Injectable} from "@angular/core";
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";
import { Login } from "./login.model";

/**
 * Created by xavi on 5/16/17.
 */
@Injectable()
export class AuthenticationService {

  constructor(private http: HttpClient) {}

  private basePath = '/api/authenticate/';

  login(loginObj: Login): any {
    return this.http.post<any>('/api/auth', loginObj);
  }

  logout(): Observable<Boolean> {
    return this.http.post<Boolean>(this.basePath + 'logout', {});
  }
}
