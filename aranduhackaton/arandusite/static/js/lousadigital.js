/**
 ** This file is part of the Arandu project.
 ** Copyright 2016 Anderson Tavares <acmt@outlook.com>.
 **
 ** This program is free software: you can redistribute it and/or modify
 ** it under the terms of the GNU General Public License as published by
 ** the Free Software Foundation, either version 3 of the License, or
 ** (at your option) any later version.
 **
 ** This program is distributed in the hope that it will be useful,
 ** but WITHOUT ANY WARRANTY; without even the implied warranty of
 ** MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 ** GNU General Public License for more details.
 **
 ** You should have received a copy of the GNU General Public License
 ** along with this program.  If not, see <http://www.gnu.org/licenses/>.
 **/

var CommandType = {
  PRESS: 1,
  MOVE: 2,
  RELEASE: 3,
  CHANGE_COLOR: 4,
  SET_WIDTH: 5
};

/**
 * @brief Class for using canvas as a drawing stream
 */
class DrawingStream{
  constructor(){
    this.canvas               = null;
    this.ctx                  = null;
    this.data                 = [];
    this.recording            = false;
    this.playing              = false;
    this.recording_start_time = 0;
    this.current_color        = null;
    this.current_event        = 0;
    this.start_time           = 0;
    this.pressed              = false;
  }
  /**
   * Get context
   *
   * @method     init
   * @param      {<type>}  namecanvas  { description }
   */
  init(namecanvas){
    this.canvas = document.getElementById(namecanvas);
    this.ctx = this.canvas.getContext('2d');
  }

  /**
   * Start recording
   *
   * @method     record
   */
  startRecording(){
    if(!this.recording){
      this.recording = true;
      var drawing = this;
      this.canvas.addEventListener("mousedown", this.downListener);
      this.canvas.addEventListener("mouseup"  , this.upListener);
      this.canvas.addEventListener("mousemove", this.moveListener);
      this.recording_start_time = new Date().getTime();
    }
  }
  pauseRecord(){
    if(this.recording){
      this.recording = false;
      this.canvas.removeEventListener("mousedown", this.downListener, null);
      this.canvas.removeEventListener("mouseup"  , this.upListener  , null);
      this.canvas.removeEventListener("mousemove", this.moveListener, null);  
    }
  }
  resetRecord(){
    this.data = [];
  }
  addChangeColorCommand(color){
    this.current_color = color;
    this.data.push([CommandType.CHANGE_COLOR  , new Date().getTime() - this.recording_start_time, this.current_color]);
  }
  changeColor(color){
    this.current_color = color;
  }

  downListener(event){
    this.data.push([CommandType.PRESS  , new Date().getTime() - this.recording_start_time, this.posX(event.clientX), this.posY(event.clientY)]);
  }
  upListener(event){
    this.data.push([CommandType.RELEASE, new Date().getTime() - this.recording_start_time, this.posX, this.posY]);
  }
  moveListener(event){
    this.data.push([CommandType.MOVE   , new Date().getTime() - this.recording_start_time, this.posX, this.posY]);
  }
  posX(X){
    return X - this.canvas.offsetLeft + document.body.scrollLeft + document.documentElement.scrollLeft;
  }
  posY(Y){
    return Y - canvas.offsetTop + document.body.scrollTop + document.documentElement.scrollTop;
  }
  
  /**
   * Play a list of drawings
   *
   * @method     play
   */
  play(){
    if(!this.playing){
      this.playing = true;
      this.start_time = new Date().getTime();
      this.current_event = 0;
      this.tick();
    }
  }

  tick(){
    if(this.playing)
      requestAnimationFrame(this.tick.bind(this));
    this.current_time = new Date().getTime();
    var duration = this.current_time - this.start_time;
    //console.log(this.current_time, this.start_time, duration, this.data[this.current_event][1]);
    if(this.data.length > this.current_event && duration > this.data[this.current_event][1]){
      this.draw();
    }
  }

  stop(){
    if(!this.playing){
      this.playing = false;
    }
  }
  
  /**
   * { function_description }
   *
   * @method     seek
   * @param      {<type>}  timestamp  { description }
   */
  seek(timestamp){

  }

  draw(){
    var video_frame = this.data[this.current_event];
    console.log(this.current_time, video_frame);
    switch(video_frame[0]){
      case CommandType.PRESS:
        this.pressed = true;
        this.ctx.moveTo(video_frame[2],video_frame[3]);
      break;
      case CommandType.MOVE:
        console.log(this.pressed);
        if(this.pressed){
          this.ctx.strokeStyle = '#00ff00';
          this.ctx.lineTo(video_frame[2],video_frame[3]);
          this.ctx.stroke();
        }
      break;
      case CommandType.RELEASE:
        this.pressed = false;
        this.ctx.moveTo(video_frame[2],video_frame[3]);
      break;
    }
    this.current_event++;
  }
  
}

class AranduRest{
  constructor(){

  }
  saveVideo(compressed, filename){

  }

  loadVideo(filename){
    var arandu = this;
    return get(filename).then(arandu.decompress).then(arandu.decodeVideo);
  }


/**
   * Decode a binary response
   *
   * @method     decode
   * @param      {<type>}  response  { description }
   */
  decodeVideo(response){

  }

  /**
   * Encode a binary response
   */
  encodeVideo(response){

  }

  /**
   * Compress the data
   *
   * @method     compress
   * @param      {<type>}  data    { description }
   */
  compress(data){

  }

  /**
   * Decompress the data
   *
   * @method     decompress
   * @param      {<type>}  data    { description }
   */
  decompress(data){

  }

}

/**
 * @brief Get a response assynchronously (JSON, XML, File...).
 * 
 * 
 * @method     get
 * @param      {<type>}  url     { description }
 * @return     {<type>}  { description_of_the_return_value }
 */
function get(url){
  return new Promise(function(resolve, reject){
    var req = new XMLHttpRequest();
    req.open('GET', url);
    req.onload = function(){
      if(req.status == 200){
        resolve(req.response);
      }else{
        reject(Error(req.statusText));
      }
    };
    req.onerror = function(){
      reject(Error("Network Error"));
    };
    req.send();
  });
}

/**
 * @brief Post a data to a server
 *
 * @method     post
 * @param      {<type>}   url     { description }
 * @param      {<type>}   blob    { description }
 * @return     {Promise}  { description_of_the_return_value }
 */
function post(url, blob){
  return new Promise(function(resolve, reject){
    var req = new XMLHttpRequest();
    req.open('POST', url, true);
    req.onload = function(){
      if(req.status == 200){
        resolve(req.response);
      }else{
        reject(Error(req.statusText));
      }
    };
    req.onerror = function(){
      reject(Error("Network Error"));
    };
    req.send(blob);
  });
}

/**
 * @brief: Agendar a execução de uma função tão logo durante
 *         um redesenho da tela. 
 * API: requestAnimFrame(funcao). Execute-a dentro da propria 
 *      `funcao` e você fará animação na página
 *
 * @param funcao Função que será executada no próximo redesenho
 *               da tela.
 * Chamando 
 */
window.requestAnimFrame = (function(){
  return window.requestAnimationFrame ||
         window.webkitRequestAnimationFrame ||
         window.mozRequestAnimationFrame ||
         function(callback){
           window.setTimeout(callback, 1000/60);
         };
})();