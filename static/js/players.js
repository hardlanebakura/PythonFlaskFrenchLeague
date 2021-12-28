var playerPosition = document.getElementsByClassName("players_player_position");

var defendersPositions = ["LB", "LCB", "CB", "RCB", "RB"];
var midfieldersPositions = ["LAM", "CAM", "RAM", "LM", "LCM", "CM", "RCM", "RM", "LWB", "LDM", "CDM", "RDM", "RWB"];
var forwardsPositions = ["LS", "ST", "RS", "LW", "LF", "CF", "RF", "RW"];

for (let i = 0; i < playerPosition.length; i++) {

    if (defendersPositions.includes(playerPosition[i].innerText)) playerPosition[i].style.backgroundColor = "green";
    else if (midfieldersPositions .includes(playerPosition[i].innerText)) playerPosition[i].style.backgroundColor = "aquamarine";
    else if (forwardsPositions.includes(playerPosition[i].innerText)) playerPosition[i].style.backgroundColor = "red";

}


