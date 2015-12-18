function init(data,viewMode){
    var svgData;
    var s = Snap('#svg');
    var svg = document.getElementById('svg');
    var image;
    svgData = {//all variables about svg + s for snap object + some configData
            's': s,
            'svg': svg,
            'width': svg.getAttribute('width'),
            'height': svg.getAttribute('height'),
            'configData': null,
            'players': [],
            'playerWithTheBall': [],
            'ball': {},
            'receiverOfTheBall': [],
            'pass': [],
            'curr': 0,
            'numOfIterations': null,
            'mode': null
        };
    if(viewMode){//if true indicates view mode
        svgData.mode = 'none'
    }
    else{
        svgData.mode = ''
    }
    image = s.image('/static/images/basketball-court.png', 0, 0, svgData.width, svgData.height);
    image.drag(function () {});//disabling drag utility for the bg image
    if(data){
        recreateData(svgData,data);
    }
    else{
        var r = svgData.width * svgData.height / 20000;
        if(r === 0){
            r = 1;
        }
        var numOfPlayers = 10;
        svgData.configData = {
                'r': r,
                'offColor': 'blue',
                'defColor': 'red',
                'numOfPlayers': numOfPlayers,
                'passTime': 500,
                'movementTime': 2000
            };
        svgData.players = createPlayers(svgData);
        svgData.ball = createBall(svgData);
    }

    document.getElementById("movePlayer").onclick = function(){
        changeMode(svgData,'movePlayer');
    };
    document.getElementById("moveBall").onclick = function(){
        changeMode(svgData,'moveBall');
    };
    document.getElementById("drawPath").onclick = function(){
        changeMode(svgData,'drawPath');
    };
    document.getElementById("drawPass").onclick = function(){
        changeMode(svgData,'drawPass');
    };
    document.getElementById("deletePath").onclick = function(){
        changeMode(svgData,'deletePath');
    };
    document.getElementById("deletePass").onclick = function(){
        changeMode(svgData,'deletePass');
    };
    document.getElementById('prevIter').onclick = function(){
        changeMode(svgData,'prevIter');
    };
    document.getElementById('nextIter').onclick = function(){
        changeMode(svgData,'nextIter');
    };
    document.getElementById('help').onclick = function(){
        var svg = document.getElementById('svgData');
        svg.innerHTML = 'numOfIter : ' + svgData.numOfIterations + '<br>' +
                    'curr : ' + svgData.curr + '<br>' +
                    'playerWithTheBall :  ' + svgData.playerWithTheBall[svgData.curr].g.attr('id');
    };
    document.getElementById('save').onclick = function(){
        changeMode(svgData,'idle');
        var i,j;
        var r = svgData.configData.r;
        var ball = svgData.ball.clone();
        var x = parseInt(svgData.playerWithTheBall[0].elem.attr('cx')) + r / 2;
        var y = parseInt(svgData.playerWithTheBall[0].elem.attr('cy')) + r / 2;
        ball.attr({'cx' : x, 'cy' : y});
        ball.remove();
        var output = {
            'configData' : svgData.configData,
            'players' : [],
            'playerWithTheBall' : [],
            'ball' : ball,
            'receiverOfTheBall' : [],
            'pass' : [],
            'numOfIterations' : svgData.numOfIterations
        };
        for(i=0;i<svgData.configData.numOfPlayers;i++) {
            output.players[i] ={
                'color' : svgData.players[i].color,
                'g' : svgData.players[i].g.clone(),
                'move' : []
            };
            if(svgData.players[i].move[0]) {
                var movePoint = svgData.players[i].move[0].getPointAtLength(0);
                output.players[i].g.select('circle').attr({ cx: movePoint.x, cy: movePoint.y });
                output.players[i].g.select('text').attr({'x':movePoint.x-r/4, 'y':movePoint.y+r/4});
            }
            output.players[i].g.remove();
            for(j=0;j<=svgData.numOfIterations;j++){
                if(svgData.players[i] === svgData.playerWithTheBall[j]){
                    output.playerWithTheBall[j] = i;
                }
                if(svgData.players[i] === svgData.receiverOfTheBall[j]){
                    output.receiverOfTheBall[j] = i;
                }
                output.players[i].move[j] = svgData.players[i].move[j];
            }
        }
        for(j=0;j<=svgData.numOfIterations;j++){
            if(svgData.pass[j]){
                output.pass[j] = svgData.pass[j];
            }
        }
        alert(JSON.stringify(output));//TODO CHANGE TO PUSH
    };
    disableButtons(svgData);
    enableButtons(svgData);
    return svgData;
}

function recreateData(svgData,data){
    var i,j;
    var s = svgData.s;

    svgData.configData = data.configData;
    svgData.numOfIterations = data.numOfIterations;
    for(i=0;i<svgData.configData.numOfPlayers;i++) {
        svgData.players[i] = {
            'color' : data.players[i].color,
            'elem' : null,
            'text' : null,
            'g' : null,
            'move' : []
        };
        svgData.players[i].elem = s.circle(data.players[i].g.childNodes[0].attr);
        svgData.players[i].text = s.text(
            data.players[i].g.childNodes[1].attr.x,
            data.players[i].g.childNodes[1].attr.y,
            data.players[i].g.childNodes[1].childNodes[0].attr.text
        );
        svgData.players[i].g = s.g(svgData.players[i].elem,svgData.players[i].text);
        svgData.players[i].g.attr({'id' : encodePlayerId(i), 'cursor' : 'default'});
        for(j=0;j<=svgData.numOfIterations;j++){
            if(data.players[i].move[j]){
                svgData.players[i].move[j] = s.path(data.players[i].move[j].attr);
                var end = svgData.s.circle(0,0,2);
                svgData.players[i].move[j].attr('markerEnd', end.marker());
                svgData.players[i].move[j].attr('display', svgData.mode);
            }
        }
    }
    for(j=0;j<=svgData.numOfIterations;j++){
        svgData.playerWithTheBall[j] = svgData.players[data.playerWithTheBall[j]];
        svgData.receiverOfTheBall[j] = svgData.players[data.receiverOfTheBall[j]];
        if(data.pass[j]){
            svgData.pass[j] = s.line(data.pass[j].attr);
            svgData.pass[j].attr('display', svgData.mode);
        }
    }
    svgData.ball = s.circle(data.ball.attr);
}

function createPlayers(svgData){
    var data, players = [];
    var i,j;
    data = calcData(svgData);

    for(i=0;i<svgData.configData.numOfPlayers;i++) {
        players[i] = createPlayer(svgData, data[i]);
    }
    for(i=0;i<=svgData.numOfIterations;i++){//using <= because numOfIterations starts from zero
        for(j=0;j<svgData.configData.numOfPlayers;j++){
            if(data[j].hasTheBall[i]){
                svgData.playerWithTheBall[i] = players[i];
            }
        }
    }
    return players;
}

function createPlayer(svgData, data){
    var s,x, y, elem, text, g, r;

    s = svgData.s;
    r = svgData.configData.r;

    x = data.position.x;
    y = data.position.y;

    elem = s.circle(x,y,r);
    text = s.text(x-r/4,y+r/4,data.label);
    text.attr('font-size',r/1.2);
    elem.attr({
        'fill':data.color
    });
    g = s.g();
    g.add(elem,text);
    g.attr('id',data.id);

    return {
        'color' : data.color,
        'elem' : elem,
        'text' : text,
        'g' : g,
        'move' : data.move
    };
}

function createBall(svgData){
    var ball, s, r, i;
    s = svgData.s;
    r = svgData.configData.r;
    var x;
    var y;

    for(i=0;i<svgData.configData.numOfPlayers;i++){
        if( svgData.players[i] === svgData.playerWithTheBall[svgData.curr]){
            x = parseInt(svgData.players[i].elem.attr('cx')) + r/2;
            y = parseInt(svgData.players[i].elem.attr('cy')) + r/2;
            ball = s.circle(x,y,r/2);
            ball.attr({
                'fill': 'brown'
            });
        }
    }
    return ball;
}

function collidesWithPlayer(svgData, player, mouseX, mouseY){
    /* expects callee to calculate relative mouse position */
    var playerX = player.elem.attr('cx');
    var playerY = player.elem.attr('cy');
    var r = svgData.configData.r;
    var touchesBall = false;
    if(Math.abs(playerX - mouseX) <= r && Math.abs(playerY - mouseY) <= r){
        touchesBall = true;
    }
    return touchesBall;
}

function calcData(svgData){
    var data = [], i;
    var numOfPlayers = svgData.configData.numOfPlayers;

    svgData.numOfIterations = 0;
    svgData.curr = 0;
    for(i=0;i<numOfPlayers;i++){
        data[i] = {
            'id' : encodePlayerId(i),
            'position' : getDefaultPosition(svgData, i),
            'color' : getColor(svgData, i),
            'label' : i%(numOfPlayers/2)+1,
            'move' : [],
            'hasTheBall' : []
        };
        data[i].move[svgData.curr] = null;
        if(i === 0){
            data[i].hasTheBall[svgData.curr] = true;
        }
        else{
            data[i].hasTheBall[svgData.curr] = false;
        }
    }
    svgData.pass[svgData.curr] = null;
    svgData.receiverOfTheBall[svgData.curr] = null;

    return data;
}

function decodePlayerId(id){
    var index;
    var pattern = /\d+/;
    index = id.match(pattern);
    return index;
}

function encodePlayerId(index){
    var id;
    id = 'svg-player-' + index;
    return id;
}

function getColor(svgData, index){
    if(index < 5){
        return svgData.configData.offColor;
    }
    else{
        return svgData.configData.defColor;
    }
}

function getDefaultPosition(svgData, index){
    var x, y, svg_width, r;
    svg_width = svgData.width;
    r = svgData.configData.r;
    y = r;

    if(index < 5){
        x = 2 * r * index + r;
    }
    else {
        x = svg_width - 2 * r * (index%5) - r;
    }
    return {'x':x,'y':y};
}

function enablePlayersMovement(svgData){
    var movePlayer = function(dx, dy, posx, posy, e) {
        posx = posx - document.getElementById('svg-container').offsetLeft;
        posy = posy - document.getElementById('svg-container').offsetTop;
        var index;
        var svg_width = svgData.width;
        var svg_height = svgData.height;
        var r = svgData.configData.r;
        if(posx-r < 0 ){
            posx = r;
        }
        if(posx+r > svg_width){
            posx = svg_width-r;
        }
        if(posy-r < 0){
            posy = r;
        }
        if(posy > svg_height){
            posy = svg_height-r;
        }
        var elem = this.select('circle');
        var text = this.select('text');
        elem.attr({'cx': posx, 'cy':posy});
        text.attr({'x':posx-r/4, 'y':posy+r/4});
        index = decodePlayerId(this.attr('id'));
        if(svgData.players[index].move[svgData.curr]) {
            var pathData = svgData.players[index].move[svgData.curr].attr('d');
            pathData = 'L' + pathData.substring(1,pathData.length);
            pathData = 'M' + posx + ',' + posy + ' ' + pathData;
            svgData.players[index].move[svgData.curr].attr('d', pathData);
        }
        if(svgData.players[index] === svgData.playerWithTheBall[svgData.curr]){
            var x = parseInt(posx) + r/2;
            var y = parseInt(posy) + r/2;
            svgData.ball.attr({'cx': x, 'cy':y});
            if(svgData.pass[svgData.curr]){
                svgData.pass[svgData.curr].attr({'x1':x,'y1':y});
            }
        }
        if(svgData.players[index] === svgData.receiverOfTheBall[svgData.curr]){
            if(svgData.pass[svgData.curr]){
                svgData.pass[svgData.curr].attr({'x2':posx,'y2':posy});
            }
        }
    };
    var startMovePlayer = function(){
        this.attr('cursor','move');
    };
    var endMovePlayer = function(){
        this.attr('cursor','grab');
    };
    for(var i=0;i<svgData.configData.numOfPlayers;i++){
        svgData.players[i].g.drag(movePlayer, startMovePlayer, endMovePlayer);
        svgData.players[i].g.attr('cursor','grab');
    }
}
function disablePlayersMovement(svgData){
    for(var i=0;i<svgData.configData.numOfPlayers;i++){
        svgData.players[i].g.undrag();
        svgData.players[i].g.drag(function(){});
        svgData.players[i].g.attr('cursor','default');
    }
}
function enableBallMovement(svgData){
    var startPosition;
    var moveBall = function(dx, dy, posx, posy, e) {
        posx = posx - document.getElementById('svg-container').offsetLeft;
        posy = posy - document.getElementById('svg-container').offsetTop;
        var svg_width = svgData.width;
        var svg_height = svgData.height;
        var r = svgData.configData.r/2;
        if(posx-r < 0 ){
            posx = r;
        }
        if(posx+r > svg_width){
            posx = svg_width-r;
        }
        if(posy-r < 0){
            posy = r;
        }
        if(posy > svg_height){
            posy = svg_height-r;
        }
        this.attr({'cx': posx, 'cy': posy});
        svgData.pass[svgData.curr].attr({'x1' : posx, 'y1' : posy});
    };
    var startMoveBall = function(){
        startPosition = {'cx' : svgData.ball.attr('cx'), 'cy' : svgData.ball.attr('cy')};
        this.attr('cursor','move');
    };
    var endMoveBall = function(e){
        var posx = e.clientX - document.getElementById('svg-container').offsetLeft;
        var posy = e.clientY - document.getElementById('svg-container').offsetTop;
        var resetBall = true;
        for(var i=0;i<svgData.configData.numOfPlayers;i++){
            if(collidesWithPlayer(svgData, svgData.players[i], posx, posy)){
                var r = svgData.configData.r;
                var player = svgData.players[i];
                var x = parseInt(player.elem.attr('cx')) + r/2;
                var y = parseInt(player.elem.attr('cy')) + r/2;
                this.attr({'cx' : x, 'cy' : y});
                svgData.playerWithTheBall[svgData.curr] = player;
                if(svgData.pass[svgData.curr]){
                    if(svgData.playerWithTheBall[svgData.curr] === svgData.receiverOfTheBall[svgData.curr] ||
                            svgData.playerWithTheBall[svgData.curr].color !== svgData.receiverOfTheBall[svgData.curr].color) {
                        svgData.pass[svgData.curr].remove();
                        svgData.pass[svgData.curr] = null;
                        svgData.receiverOfTheBall[svgData.curr] = null;
                    }
                    else{
                        svgData.pass[svgData.curr].attr({'x1' : x, 'y1' : y});
                    }
                }
                resetBall = false;
                break;
            }
        }
        if(resetBall){
            this.attr(startPosition);
            if(svgData.pass[svgData.curr]){
                svgData.pass[svgData.curr].attr({'x1' : startPosition.cx, 'y1' : startPosition.cy});
            }
        }
        this.attr('cursor','grab');
    };
    svgData.ball.drag(moveBall, startMoveBall, endMoveBall);
    svgData.ball.attr('cursor','grab');
}

function disableBallMovement(svgData){
    svgData.ball.undrag();
    svgData.ball.drag(function(){});
    svgData.ball.attr('cursor','default');
}

function enableDrawingPath(svgData){
    var startPosition;
    var drawing = false;
    var playerMoving = null;
    var continueDrawingPath = function(e) {
        var posx = e.clientX - document.getElementById('svg-container').offsetLeft;
        var posy = e.clientY - document.getElementById('svg-container').offsetTop;
        if(drawing){
            var pathData = playerMoving.move[svgData.curr].attr("d");
            pathData = pathData + " L" + posx + "," + posy;
            playerMoving.move[svgData.curr].attr("d", pathData);
        }
    };
    var startDrawingPath = function(e){
        var posx = e.clientX - document.getElementById('svg-container').offsetLeft;
        var posy = e.clientY - document.getElementById('svg-container').offsetTop;
        for(var i=0;i<svgData.configData.numOfPlayers;i++){
            if(collidesWithPlayer(svgData, svgData.players[i], posx, posy)){
                playerMoving = svgData.players[i];
                if(playerMoving.move[svgData.curr]){
                    for(var j=svgData.curr;j<=svgData.numOfIterations;j++){
                        //TODO check if conflicts, cause no change to numOfIterations;
                        if(playerMoving.move[j]){
                            playerMoving.move[j].remove();
                            playerMoving.move[j] = null;
                        }
                        if(j != svgData.curr && svgData.pass[j]) {
                            if (svgData.playerWithTheBall[j] === playerMoving
                                    || svgData.receiverOfTheBall[j] === playerMoving) {
                                for (var k = j; k <= svgData.numOfIterations; k++) {
                                    //TODO check if conflicts, cause no change to numOfIterations;
                                    if (svgData.pass[k]) {
                                        svgData.pass[k].remove();
                                        svgData.pass[k] = null;
                                    }
                                    svgData.playerWithTheBall[k] = svgData.playerWithTheBall[j];
                                    svgData.receiverOfTheBall[k] = null;
                                }
                            }
                        }
                    }
                }
                playerMoving.move[svgData.curr] = null;

                startPosition = {'cx' : playerMoving.elem.attr('cx'), 'cy' : playerMoving.elem.attr('cy')};
                this.attr('cursor','pointer');
                playerMoving.move[svgData.curr] = svgData.s.path('');
                playerMoving.move[svgData.curr].attr("fill", "none");
                playerMoving.move[svgData.curr].attr("stroke", playerMoving.color);
                playerMoving.move[svgData.curr].attr("stroke-width", 2);
                playerMoving.move[svgData.curr].attr("stroke-linecap", "round");
                playerMoving.move[svgData.curr].attr(
                        "d", "M" + startPosition.cx  + "," + startPosition.cy + ' L' + posx + ','+ posy
                );

                var end = svgData.s.circle(0,0,2);
                playerMoving.move[svgData.curr].attr('markerEnd', end.marker());
                drawing = true;
            }
        }
    };
    var endDrawingPath = function(e){
        drawing = false;
        this.attr('cursor','default');
    };
    svgData.s.mousedown(startDrawingPath);
    svgData.s.mousemove(continueDrawingPath);
    svgData.s.mouseup(endDrawingPath);
    for(var i=0;i<svgData.configData.numOfPlayers;i++){
        svgData.players[i].g.attr('cursor','pointer');
    }

}
function disableDrawingPath(svgData){
    var path = false;
    svgData.s.unmousedown();
    svgData.s.unmousemove();
    svgData.s.unmouseup();
    for(var i=0;i<svgData.configData.numOfPlayers;i++){
        svgData.players[i].g.attr('cursor','default');
        if(svgData.players[i].move[svgData.curr]){
            path = true;
        }
    }
    if(path || svgData.pass[svgData.curr]){
        if(svgData.curr === svgData.numOfIterations){
            svgData.numOfIterations++;
            if(svgData.pass[svgData.curr]){
                svgData.playerWithTheBall[svgData.numOfIterations] = svgData.receiverOfTheBall[svgData.curr];
            }
            else{
                svgData.playerWithTheBall[svgData.numOfIterations] = svgData.playerWithTheBall[svgData.curr];
            }
            svgData.pass[svgData.numOfIterations] = null;
            svgData.receiverOfTheBall[svgData.numOfIterations] = null;
            for(i=0;i<svgData.configData.numOfPlayers;i++){
                svgData.players[i].move[svgData.numOfIterations] = null;
            }
        }
    }
}
function enableDrawingPass(svgData){
    var startPosition;
    var drawing = false;
    var continueDrawingPass = function(e) {
        var posx = e.clientX - document.getElementById('svg-container').offsetLeft;
        var posy = e.clientY - document.getElementById('svg-container').offsetTop;
        if(drawing){
            svgData.pass[svgData.curr].attr({'x2' : posx, 'y2' : posy});
        }
    };
    var startDrawingPass = function(e){
        var posx = e.clientX - document.getElementById('svg-container').offsetLeft;
        var posy = e.clientY - document.getElementById('svg-container').offsetTop;
        if(collidesWithPlayer(svgData, svgData.playerWithTheBall[svgData.curr], posx, posy)){
            if(svgData.pass[svgData.curr]){
                svgData.pass[svgData.curr].remove();
            }
            startPosition = {
                'cx' : svgData.playerWithTheBall[svgData.curr].elem.attr('cx'),
                'cy' : svgData.playerWithTheBall[svgData.curr].elem.attr('cy')
            };
            drawing = true;
            this.attr('cursor','no-drop');
            for(var i=0;i<svgData.configData.numOfPlayers; i++){
                if(svgData.players[i].color === svgData.playerWithTheBall[svgData.curr].color) {
                    svgData.players[i].g.attr('cursor', 'crosshair');
                }
                else{
                    svgData.players[i].g.attr('cursor', 'no-drop');
                }
            }
            svgData.playerWithTheBall[svgData.curr].g.attr('cursor','no-drop');
            var r = svgData.configData.r;
            var x = parseInt(startPosition.cx) + r/2;
            var y = parseInt(startPosition.cy) + r/2;
            svgData.pass[svgData.curr] = svgData.s.line(x,y,posx,posy);
            svgData.pass[svgData.curr].attr("stroke", 'brown');
            svgData.pass[svgData.curr].attr("stroke-width", 2);
            svgData.pass[svgData.curr].attr("stroke-linecap", "round");
            svgData.pass[svgData.curr].attr("stroke-dasharray", "10,10");
        }
    };
    var endDrawingPass = function(e){
        var i,j;
        var posx = e.clientX - document.getElementById('svg-container').offsetLeft;
        var posy = e.clientY - document.getElementById('svg-container').offsetTop;
        if(drawing) {
            var clearPass = true;
            for (i = 0; i < svgData.configData.numOfPlayers; i++) {
                if (svgData.playerWithTheBall[svgData.curr] !== svgData.players[i]) {
                    if(svgData.players[i].color === svgData.playerWithTheBall[svgData.curr].color) {
                        if (collidesWithPlayer(svgData, svgData.players[i], posx, posy)) {
                            if(svgData.players[i] !== svgData.receiverOfTheBall[svgData.curr]){
                                for(j=svgData.curr+1;j<=svgData.numOfIterations;j++){
                                    //TODO check if conflicts, cause no change to numOfIterations;
                                    if(svgData.pass[j]){
                                        svgData.pass[j].remove();
                                        svgData.pass[j] = null;
                                    }
                                    svgData.playerWithTheBall[j] = svgData.playerWithTheBall[svgData.curr];
                                    svgData.receiverOfTheBall[j] = null;
                                }
                            }
                            svgData.pass[svgData.curr].attr({
                                'x2' : svgData.players[i].elem.attr('cx'),
                                'y2' : svgData.players[i].elem.attr('cy')}
                            );
                            svgData.receiverOfTheBall[svgData.curr] = svgData.players[i];
                            svgData.playerWithTheBall[svgData.curr+1] = svgData.receiverOfTheBall[svgData.curr];
                            clearPass = false;
                            break;
                        }
                    }
                }
            }
            if (clearPass) {
                svgData.pass[svgData.curr].remove();
                svgData.pass[svgData.curr] = null;
                svgData.receiverOfTheBall[svgData.curr] = null;
                svgData.playerWithTheBall[svgData.curr+1] = svgData.playerWithTheBall[svgData.curr];
                for(j=svgData.curr+1;j<=svgData.numOfIterations;j++){
                    //TODO check if conflicts, cause no change to numOfIterations;
                    if(svgData.pass[j]){
                        svgData.pass[j].remove();
                        svgData.pass[j] = null;
                    }
                    svgData.playerWithTheBall[j] = svgData.playerWithTheBall[svgData.curr];
                    svgData.receiverOfTheBall[j] = null;
                }
            }
            for(i=0;i<svgData.configData.numOfPlayers; i++){
                svgData.players[i].g.attr('cursor', 'default');
            }
            svgData.playerWithTheBall[svgData.curr].g.attr('cursor','pointer');
            this.attr('cursor','default');
        }
        drawing = false;
    };
    svgData.s.mousedown(startDrawingPass);
    svgData.s.mousemove(continueDrawingPass);
    svgData.s.mouseup(endDrawingPass);
    svgData.playerWithTheBall[svgData.curr].g.attr('cursor','pointer');
}
function disableDrawingPass(svgData){
    var path = false;
    svgData.s.unmousedown();
    svgData.s.unmousemove();
    svgData.s.unmouseup();
    svgData.playerWithTheBall[svgData.curr].g.attr('cursor','default');

    for(var i=0;i<svgData.configData.numOfPlayers;i++){
        if(svgData.players[i].move[svgData.curr]){
            path = true;
        }
    }
    if(path || svgData.pass[svgData.curr]){
        if(svgData.curr === svgData.numOfIterations){
            svgData.numOfIterations++;

            svgData.pass[svgData.numOfIterations] = null;
            svgData.receiverOfTheBall[svgData.numOfIterations] = null;
            for(i=0;i<svgData.configData.numOfPlayers;i++){
                svgData.players[i].move[svgData.numOfIterations] = null;
            }
        }
    }
}
function enableDeletePath(svgData){
    for(var i=0;i<svgData.configData.numOfPlayers;i++){
        if(svgData.players[i].move[svgData.curr]){
            svgData.players[i].g.attr('cursor','crosshair');
            svgData.players[i].move[svgData.curr].attr('cursor','crosshair');
            svgData.players[i].g.click(function(index){
                return function(){
                    var i;
                    if(svgData.players[index].move[svgData.curr]){
                        svgData.players[index].g.attr('cursor','default');
                        svgData.players[index].move[svgData.curr].attr('cursor','default');
                        for(var j=svgData.curr;j<=svgData.numOfIterations;j++){
                            //TODO check if conflicts, cause no change to numOfIterations;
                            if(svgData.players[index].move[j]){
                                svgData.players[index].move[j].remove();
                                svgData.players[index].move[j] = null;
                            }
                            if(j != svgData.curr && svgData.pass[j]) {
                                if (svgData.playerWithTheBall[j] === svgData.players[index]
                                        || svgData.receiverOfTheBall[j] === svgData.players[index]) {
                                    for (i = j; i <= svgData.numOfIterations; i++) {
                                        //TODO check if conflicts, cause no change to numOfIterations;
                                        if (svgData.pass[i]) {
                                            svgData.pass[i].remove();
                                            svgData.pass[i] = null;
                                        }
                                        svgData.playerWithTheBall[i] = svgData.players[index];
                                        svgData.receiverOfTheBall[i] = null;
                                    }
                                }
                            }
                        }
                    }
                };
            }(i));
            svgData.players[i].move[svgData.curr].click(function(index){
                return function(){
                    var i;
                    if(svgData.players[index].move[svgData.curr]){
                        svgData.players[index].g.attr('cursor','default');
                        svgData.players[index].move[svgData.curr].attr('cursor','default');
                        for(var j=svgData.curr;j<=svgData.numOfIterations;j++){
                            //TODO check if conflicts, cause no change to numOfIterations;
                            if(svgData.players[index].move[j]){
                                svgData.players[index].move[j].remove();
                                svgData.players[index].move[j] = null;
                            }
                            if(j != svgData.curr && svgData.pass[j]) {
                                if (svgData.playerWithTheBall[j] === svgData.players[index]
                                        || svgData.receiverOfTheBall[j] === svgData.players[index]) {
                                    for (i = j; i <= svgData.numOfIterations; i++) {
                                        //TODO check if conflicts, cause no change to numOfIterations;
                                        if (svgData.pass[i]) {
                                            svgData.pass[i].remove();
                                            svgData.pass[i] = null;
                                        }
                                        svgData.playerWithTheBall[i] = svgData.players[index];
                                        svgData.receiverOfTheBall[i] = null;
                                    }
                                }
                            }
                        }
                    }
                };
            }(i));
        }
    }
}
function disableDeletePath(svgData){
    var path = false;
    for(var i=0;i<svgData.configData.numOfPlayers;i++){
        if(svgData.players[i].move[svgData.curr]){
            svgData.players[i].g.attr('cursor','default');
            svgData.players[i].move[svgData.curr].attr('cursor','default');
            svgData.players[i].g.unclick();
            svgData.players[i].move[svgData.curr].unclick();
            path = true;
        }
    }
    if(!path && !svgData.pass[svgData.curr]){
        if(svgData.curr != svgData.numOfIterations) {
            if (svgData.curr > 0) {
                svgData.numOfIterations--;
            }
        }
    }
}
function enableDeletePass(svgData){
    if(svgData.pass[svgData.curr]){
        var clearPass = function(){
            if(svgData.pass[svgData.curr]){
                svgData.receiverOfTheBall[svgData.curr].g.attr('cursor', 'default');
                svgData.playerWithTheBall[svgData.curr].g.attr('cursor', 'default');
                svgData.ball.attr('cursor', 'default');
                svgData.pass[svgData.curr].remove();
                svgData.pass[svgData.curr] = null;
                svgData.receiverOfTheBall[svgData.curr] = null;
                for(var j=svgData.curr+1;j<=svgData.numOfIterations;j++){
                    //TODO check if conflicts, cause no change to numOfIterations;
                    if(svgData.pass[j]){
                        svgData.pass[j].remove();
                        svgData.pass[j] = null;
                    }
                    svgData.playerWithTheBall[j] = svgData.playerWithTheBall[svgData.curr];
                    svgData.receiverOfTheBall[j] = null;
                }
            }
        };
        svgData.pass[svgData.curr].click(clearPass);
        svgData.playerWithTheBall[svgData.curr].g.click(clearPass);
        svgData.ball.click(clearPass);
        svgData.receiverOfTheBall[svgData.curr].g.click(clearPass);
        svgData.pass[svgData.curr].attr('cursor', 'crosshair');
        svgData.playerWithTheBall[svgData.curr].g.attr('cursor', 'crosshair');
        svgData.ball.attr('cursor', 'crosshair');
        svgData.receiverOfTheBall[svgData.curr].g.attr('cursor', 'crosshair');
    }
}
function disableDeletePass(svgData){
    if(svgData.pass[svgData.curr]){
        svgData.pass[svgData.curr].unclick();
        svgData.receiverOfTheBall[svgData.curr].g.unclick();
        svgData.pass[svgData.curr].attr('cursor', 'default');
        svgData.receiverOfTheBall[svgData.curr].g.attr('cursor', 'default');
    }
    else{
        var path = false;
        for(var i=0;i<svgData.configData.numOfPlayers;i++){
            if(svgData.players[i].move[svgData.curr]){
                path = true;
            }
        }
        if(!path){
            if(svgData.curr != svgData.numOfIterations) {
                if (svgData.curr > 0) {
                    svgData.numOfIterations--;
                }
            }
        }
    }
    svgData.playerWithTheBall[svgData.curr].g.unclick();
    svgData.ball.unclick();
    svgData.playerWithTheBall[svgData.curr].g.attr('cursor', 'default');
    svgData.ball.attr('cursor', 'default');
}

function doMoves(svgData){
    var x, y, r;
    var movePlayers = function(){
        for(var i=0;i<svgData.configData.numOfPlayers;i++){
            if(svgData.players[i].move[svgData.curr]){
                var len = svgData.players[i].move[svgData.curr].getTotalLength();
                svgData.players[i].move[svgData.curr].attr('display', 'none');
                (function(i,len, lastPlayerMovingIndex){
                    Snap.animate(
                            0,
                            len,
                            function(value) {
                                var x, y;
                                var player = svgData.players[i];
                                var r = svgData.configData.r;
                                var movePoint = player.move[svgData.curr].getPointAtLength(value);
                                player.elem.attr({ cx: movePoint.x, cy: movePoint.y });
                                player.text.attr({'x':movePoint.x-r/4, 'y':movePoint.y+r/4});
                                if(svgData.pass[svgData.curr]) {
                                    if(player === svgData.receiverOfTheBall[svgData.curr]) {
                                        x = movePoint.x + r / 2;
                                        y = movePoint.y + r / 2;
                                        svgData.ball.attr({'cx': x, 'cy': y});
                                    }
                                }
                                else{
                                    if(player === svgData.playerWithTheBall[svgData.curr]){
                                        x = movePoint.x + r / 2;
                                        y = movePoint.y + r / 2;
                                        svgData.ball.attr({'cx': x, 'cy': y});
                                    }
                                }
                            },
                            svgData.configData.movementTime,
                            mina.linear,
                            function(){
                                if(svgData.curr < svgData.numOfIterations){
                                    if(i == lastPlayerMovingIndex) {
                                        svgData.curr++;
                                        enableButtons(svgData);
                                    }
                                }
                            }
                    );
                })(i,len,lastPlayerMovingIndex);
            }
        }
    };
    var playersMoving = false;
    var lastPlayerMovingIndex = 0;
    for(var i=0;i<svgData.configData.numOfPlayers;i++){
        if(svgData.players[i].move[svgData.curr]){
            playersMoving = true;
            if(i > lastPlayerMovingIndex){
                lastPlayerMovingIndex = i;
            }
        }
    }
    if(playersMoving || svgData.pass[svgData.curr]){
        disableButtons(svgData);
    }
    if(svgData.pass[svgData.curr]){
        svgData.pass[svgData.curr].attr('display', 'none');
        r = svgData.configData.r;
        x = parseInt(svgData.receiverOfTheBall[svgData.curr].elem.attr('cx')) + r / 2;
        y = parseInt(svgData.receiverOfTheBall[svgData.curr].elem.attr('cy')) + r / 2;
        if(!playersMoving){
            svgData.ball.animate(
                    {
                        'cx' : x,
                        'cy' : y
                    },
                    svgData.configData.passTime,
                    mina.linear,
                    function(){
                        if(svgData.curr < svgData.numOfIterations){
                            svgData.curr++;
                            enableButtons(svgData);
                        }
                    }
            );
        }
        else{
            svgData.ball.animate(
                    {
                        'cx' : x,
                        'cy' : y
                    },
                    svgData.configData.passTime,
                    mina.linear,
                    movePlayers
            );
        }
    }
    else{
        if(playersMoving) {
            movePlayers();
        }
    }
}

function resetMoves(svgData){
    var reset = function(){
        var r = svgData.configData.r;
        for(var i=0;i<svgData.configData.numOfPlayers;i++){
            if(svgData.players[i].move[svgData.curr]){
                var movePoint = svgData.players[i].move[svgData.curr].getPointAtLength(0);
                svgData.players[i].elem.attr({ cx: movePoint.x, cy: movePoint.y });
                svgData.players[i].text.attr({'x':movePoint.x-r/4, 'y':movePoint.y+r/4});
                svgData.players[i].move[svgData.curr].attr('display', svgData.mode);
            }
        }
        var x = parseInt(svgData.playerWithTheBall[svgData.curr].elem.attr('cx')) + r / 2;
        var y = parseInt(svgData.playerWithTheBall[svgData.curr].elem.attr('cy')) + r / 2;
        svgData.ball.attr({'cx' : x, 'cy' : y});
        if(svgData.pass[svgData.curr]){
            svgData.pass[svgData.curr].attr('display', svgData.mode);
        }
    };
    reset();
}

function changeMode(svgData, mode){
    switch(mode){
        case 'movePlayer':
            disableBallMovement(svgData);
            disableDrawingPath(svgData);
            disableDrawingPass(svgData);
            disableDeletePath(svgData);
            disableDeletePass(svgData);
            enablePlayersMovement(svgData);
            break;
        case 'moveBall':
            disablePlayersMovement(svgData);
            disableDrawingPath(svgData);
            disableDrawingPass(svgData);
            disableDeletePath(svgData);
            disableDeletePass(svgData);
            enableBallMovement(svgData);
            break;
        case 'drawPath':
            disablePlayersMovement(svgData);
            disableBallMovement(svgData);
            disableDrawingPass(svgData);
            disableDeletePath(svgData);
            disableDeletePass(svgData);
            enableDrawingPath(svgData);
            break;
        case 'drawPass':
            disablePlayersMovement(svgData);
            disableBallMovement(svgData);
            disableDrawingPath(svgData);
            disableDeletePath(svgData);
            disableDeletePass(svgData);
            enableDrawingPass(svgData);
            break;
        case 'deletePath':
            disablePlayersMovement(svgData);
            disableBallMovement(svgData);
            disableDrawingPath(svgData);
            disableDrawingPass(svgData);
            disableDeletePass(svgData);
            enableDeletePath(svgData);
            break;
        case 'deletePass':
            disablePlayersMovement(svgData);
            disableBallMovement(svgData);
            disableDrawingPath(svgData);
            disableDrawingPass(svgData);
            disableDeletePath(svgData);
            enableDeletePass(svgData);
            break;
        case 'prevIter':
            if(svgData.curr > 0){
                svgData.curr--;
                resetMoves(svgData);
                enableButtons(svgData);
            }
            break;
        case 'nextIter':
            resetMoves(svgData);
            disablePlayersMovement(svgData);
            disableBallMovement(svgData);
            disableDrawingPath(svgData);
            disableDrawingPass(svgData);
            disableDeletePath(svgData);
            disableDeletePass(svgData);
            doMoves(svgData);
            break;
        default:/* idle */
            disablePlayersMovement(svgData);
            disableBallMovement(svgData);
            disableDrawingPath(svgData);
            disableDrawingPass(svgData);
            disableDeletePath(svgData);
            disableDeletePass(svgData);
    }
}
function enableButtons(svgData){
    if(svgData.mode === '') {//indicates edit mode is on
        if (svgData.curr === 0) {
            document.getElementById("movePlayer").disabled = false;
            document.getElementById("moveBall").disabled = false;
        }
        document.getElementById("drawPath").disabled = false;
        document.getElementById("drawPass").disabled = false;
        document.getElementById("deletePath").disabled = false;
        document.getElementById("deletePass").disabled = false;
        document.getElementById("save").disabled = false;
    }
    document.getElementById('prevIter').disabled = false;
    document.getElementById('nextIter').disabled = false;
}
function disableButtons(svgData){
    if(svgData.mode === '') {//indicates edit mode is on
        document.getElementById("movePlayer").disabled = true;
        document.getElementById("moveBall").disabled = true;
        document.getElementById("drawPath").disabled = true;
        document.getElementById("drawPass").disabled = true;
        document.getElementById("deletePath").disabled = true;
        document.getElementById("deletePass").disabled = true;
        document.getElementById("save").disabled = true;
    }
    document.getElementById('prevIter').disabled = true;
    document.getElementById('nextIter').disabled = true;
}
