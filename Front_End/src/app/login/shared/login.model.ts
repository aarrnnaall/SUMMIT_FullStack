
export class Login {

  public name: string;
  public pwd: string;
  constructor( object: any){
    this.name = (object.username) ? object.username : null;
    this.pwd = (object.password) ? object.password : null;
  }
}
