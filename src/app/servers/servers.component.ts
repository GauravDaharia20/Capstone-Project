import { NULL_EXPR } from '@angular/compiler/src/output/output_ast';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-servers',
  templateUrl: './servers.component.html',
  styles: [`

  .online {
      color:white;
  }
  `]
})
export class ServersComponent implements OnInit {


  id = 10;
  status="offline";
  allowServer=false;
  serverCreation = "No server Created yet";
  serverName=''
  serverCreated=false;

  servers = ['testserver1','testserver2'];


  userName=''
  allowUser=false;
  constructor() {
    setTimeout(()=>{
      this.allowServer=true;
    },1000)

    this.status = Math.random() > 0.5 ? 'online' : 'offline';


   }

   getColor(){
     return this.status === 'online' ? 'green' : 'red'; 
   }

   updateUserButton()
   {
     this.userName='';
   }

   onServerCreation() {
     this.servers.push(this.serverName);
      this.serverCreation = "Server is Created "+this.serverName;
      this.serverCreated=true;     
   }
  
   UpdateServer(event:any){
    //console.log(event)
    this.serverName=(<HTMLInputElement>event.target).value;
   }

   clearText(){
     this.serverName='';
   }

  ngOnInit(): void {
  }

}
