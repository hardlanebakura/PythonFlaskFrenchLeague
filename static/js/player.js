var releaseClauseInEur = document.getElementsByClassName("player_profile_info_1_1_content")[3];
var playerValueEur = document.getElementsByClassName("player_value_1")[0];
var playerWageInEur = document.getElementsByClassName("player_wage_1")[0];
var playerSpecialties = document.getElementsByClassName("player_profile_player_specialties")[0].childNodes;
var playerProfileInfoHeader = document.getElementsByClassName("player_profile_info_header")[2];
var playerPositions = document.getElementsByClassName("player_position_1");
var playerAbilityValues = document.getElementsByClassName("player_abilities_value");
var playerOverallRating = document.getElementsByClassName("player_overall_rating_1")[0];
var playerPotential = document.getElementsByClassName("player_potential_1")[0];
var dob = document.getElementsByClassName("player_player_dob")[0];
var tier1Skills = "#0c8539";
var tier2Skills = "#66a80f";
var tier3Skills = "#e6b600";
var tier4Skills = "#ff0000";

const moneyToMillions = (startNumber) => {

    var startValue = parseInt(startNumber.innerText);
    if (startValue < 999) startNumber.innerText = "€" + startValue.toString();
    else if (startValue > 999 && startValue < 1000000) startNumber.innerText = "€" + (startValue/1000).toString() + "K";
    else if (startValue > 1000000) { startNumber.innerText = "€" + (startValue/1000000).toString() + "M"; console.log("1"); }
    return startNumber.innerText;

}

releaseClauseInEur.innerText = moneyToMillions(releaseClauseInEur);
playerValueEur.innerText = moneyToMillions(playerValueEur);
playerWageInEur.innerText = moneyToMillions(playerWageInEur);

console.log(playerProfileInfoHeader.length);

var playerPosition = document.getElementsByClassName("players_player_position");

var defendersPositions = ["LB", "LCB", "CB", "RCB", "RB"];
var midfieldersPositions = ["LAM", "CAM", "RAM", "LM", "LCM", "CM", "RCM", "RM", "LWB", "LDM", "CDM", "RDM", "RWB"];
var forwardsPositions = ["LS", "ST", "RS", "LW", "LF", "CF", "RF", "RW"];

for (let i = 0; i < playerPosition.length; i++) {

    if (defendersPositions.includes(playerPosition[i].innerText)) playerPosition[i].style.backgroundColor = "green";
    else if (midfieldersPositions .includes(playerPosition[i].innerText)) playerPosition[i].style.backgroundColor = "aquamarine";
    else if (forwardsPositions.includes(playerPosition[i].innerText)) playerPosition[i].style.backgroundColor = "red";

}

const skillsValuesColors = (skillsValue) => {

    if (parseInt(skillsValue.innerText) > 79) skillsValue.style.backgroundColor = tier1Skills;
    else if (parseInt(skillsValue.innerText) > 69) skillsValue.style.backgroundColor = tier2Skills;
    else if (parseInt(skillsValue.innerText) > 59) skillsValue.style.backgroundColor = tier3Skills;

}

console.log(playerPositions.length);

for (let i = 0; i < playerPositions.length; i++) {

    let positionValue = playerPositions[i].childNodes[3];
    console.log(positionValue);
    var values = positionValue.innerText.split("+");
    var values1 = positionValue.innerText.split("-");

    if (i == playerPositions.length - 1) {
    if (typeof(m) == "undefined") playerPositions[i].style.transform = "translate(140px,-441px)";
    else playerPositions[i].style.transform = "translate(140px, -78px)";
    }
    console.log(!(typeof(m) == "undefined"));
    if (values.length > 1) {
        let sum = parseInt(values[0]) + parseInt(values[1]);
        positionValue.innerText = sum;
        console.log(sum);
        console.log(i);
        if (sum > 79) playerPositions[i].style.backgroundColor = tier1Skills;
        else if (sum > 69) playerPositions[i].style.backgroundColor = tier2Skills;
        else if (sum > 59) playerPositions[i].style.backgroundColor = tier3Skills;
        else playerPositions[i].style.backgroundColor = tier4Skills;
    }
    else {
        let sum = positionValue.innerText;
        if (sum > 79) playerPositions[i].style.backgroundColor = tier1Skills;
        else if (sum > 69) playerPositions[i].style.backgroundColor = tier2Skills;
        else if (sum > 59) playerPositions[i].style.backgroundColor = tier3Skills;
        else playerPositions[i].style.backgroundColor = tier4Skills;
    }

    if (values1.length > 1) {
        let sum = parseInt(values1[0]) - parseInt(values1[1]);
        positionValue.innerText = sum;
        console.log(sum);
        console.log(i);
        if (sum > 79) playerPositions[i].style.backgroundColor = tier1Skills;
        else if (sum > 69) playerPositions[i].style.backgroundColor = tier2Skills;
        else if (sum > 59) playerPositions[i].style.backgroundColor = tier3Skills;
        else playerPositions[i].style.backgroundColor = tier4Skills;
    }
    else {
        let sum = positionValue.innerText;
        if (sum > 79) playerPositions[i].style.backgroundColor = tier1Skills;
        else if (sum > 69) playerPositions[i].style.backgroundColor = tier2Skills;
        else if (sum > 59) playerPositions[i].style.backgroundColor = tier3Skills;
        else playerPositions[i].style.backgroundColor = tier4Skills;
    }

}

for (let i = 0; i < playerAbilityValues.length; i++) skillsValuesColors(playerAbilityValues[i]);
skillsValuesColors(playerOverallRating);
skillsValuesColors(playerPotential);
console.log(playerProfileInfoHeader.innerText);
playerProfileInfoHeader.innerText = playerProfileInfoHeader.innerText.toUpperCase();

const formatDate = (date) => {

    date = date.split("-");
    dateMonths = date[1];
    let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let selectedIndex = parseInt(dateMonths) - 1;
    let month = months[selectedIndex].slice(0,3);
    let formattedDate = `${month}` + " " + date[2] + ", " + date[0];
    return formattedDate;

}

dob.innerText = formatDate(dob.innerText);

var clubJoinedDate = document.getElementsByClassName("player_profile_club_joined_value")[0];
clubJoinedDate.innerText = formatDate(clubJoinedDate.innerText);

var playerDiagramRating = document.getElementsByClassName("player_diagram_player_overall");
var playerDiagramPotential = document.getElementsByClassName("player_diagram_player_potential");
var playerDiagramPlayerPosition = document.getElementsByClassName("player_diagram_player_position");

for (let i = 0; i < playerDiagramRating.length; i++) {

    skillsValuesColors(playerDiagramRating[i]);
    skillsValuesColors(playerDiagramPotential[i]);

}

for (let i = 0; i < playerDiagramPlayerPosition.length; i++) {

    if (defendersPositions.includes(playerDiagramPlayerPosition[i].innerText)) playerDiagramPlayerPosition[i].style.color = "green";
    else if (midfieldersPositions .includes(playerDiagramPlayerPosition[i].innerText)) playerDiagramPlayerPosition[i].style.color = "aquamarine";
    else if (forwardsPositions.includes(playerDiagramPlayerPosition[i].innerText)) playerDiagramPlayerPosition[i].style.color = "red";
    else {
    playerDiagramPlayerPosition[i].style.backgroundColor = "yellow";
    playerDiagramPlayerPosition[i].style.color = "#000";
    playerDiagramPlayerPosition[i].style.paddingTop = "4px";
    playerDiagramPlayerPosition[i].style.marginTop = "0px";
    }


}












