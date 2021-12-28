var teamImages = document.getElementsByTagName("img");
console.log(teamImages.length);

var highestMatchCapacity = !(typeof(highest_match_capacity) === 'undefined');
if (highestMatchCapacity) {

    var teamTopScorers = document.getElementsByClassName("team_top_scorers");
    teamTopScorers[1].style.height = "303px";



var statisticsOneMatch = document.getElementsByClassName("statistics_one_match");

//css improving
for (let i = 0; i < 3; i++) {

    statisticsOneMatch[i].childNodes[1].style.paddingLeft = "0";
    statisticsOneMatch[i].childNodes[1].style.marginLeft = "-10px";
    statisticsOneMatch[i].childNodes[1].childNodes[3].style.paddingTop = "10px";
    statisticsOneMatch[i].childNodes[1].childNodes[3].style.paddingLeft = "14px";
    statisticsOneMatch[i].childNodes[1].childNodes[5].style.paddingTop = "10px";
    statisticsOneMatch[i].childNodes[1].childNodes[5].style.paddingLeft = "48px";
    statisticsOneMatch[i].childNodes[3].childNodes[1].style.marginLeft = "19px";
    statisticsOneMatch[i].childNodes[3].childNodes[3].style.marginLeft = "-22px";
    statisticsOneMatch[i].childNodes[3].childNodes[5].style.marginLeft = "31px";
    statisticsOneMatch[1].childNodes[1].childNodes[3].style.marginLeft = "17px";
    statisticsOneMatch[1].childNodes[3].childNodes[3].style.marginLeft = "-4px";
    statisticsOneMatch[2].childNodes[3].style.marginTop = "17px";
    statisticsOneMatch[2].childNodes[1].childNodes[1].style.marginLeft = "40px";
    statisticsOneMatch[2].childNodes[1].childNodes[3].style.marginLeft = "4px";
    statisticsOneMatch[2].childNodes[1].childNodes[5].style.marginLeft = "1px";
    statisticsOneMatch[2].childNodes[5].childNodes[1].style.marginLeft = "22px";
    statisticsOneMatch[2].childNodes[5].childNodes[3].style.marginLeft = "-9px";
    statisticsOneMatch[2].childNodes[5].childNodes[5].style.marginLeft = "18px";
    statisticsOneMatch[2].childNodes[1].childNodes[5].style.paddingLeft = "1px";

}

}

var tier1Skills = "#0c8539";
var tier2Skills = "#66a80f";
var tier3Skills = "#e6b600";
var tier4Skills = "#ff0000";
var defendersPositions = ["LB", "LCB", "CB", "RCB", "RB"];
var midfieldersPositions = ["LAM", "CAM", "RAM", "LM", "LCM", "CM", "RCM", "RM", "LWB", "LDM", "CDM", "RDM", "RWB"];
var forwardsPositions = ["LS", "ST", "RS", "LW", "LF", "CF", "RF", "RW"];

function skillsValuesColors(skillsValue) {

    if (parseInt(skillsValue.innerText) > 79) skillsValue.style.backgroundColor = tier1Skills;
    else if (parseInt(skillsValue.innerText) > 69) skillsValue.style.backgroundColor = tier2Skills;
    else if (parseInt(skillsValue.innerText) > 59) skillsValue.style.backgroundColor = tier3Skills;

}

function positionsColors(playerPosition) {

    if (defendersPositions.includes(playerPosition.innerText)) playerPosition.style.backgroundColor = "green";
    else if (midfieldersPositions .includes(playerPosition.innerText)) playerPosition.style.backgroundColor = "aquamarine";
    else if (forwardsPositions.includes(playerPosition.innerText)) playerPosition.style.backgroundColor = "red";

}

const moneyToMillions = (startNumber) => {

    var startValue = parseInt(startNumber.innerText);
    if (startValue < 999) startNumber.innerText = "€" + startValue.toString();
    else if (startValue > 999 && startValue < 1000000) startNumber.innerText = "€" + ((startValue/1000).toFixed(2)).toString() + "K";
    else if (startValue > 1000000) { startNumber.innerText = "€" + ((startValue/1000000).toFixed(2)).toString() + "M"; }
    return startNumber.innerText;

}

var teamSalaries = !(typeof(team_salaries) === 'undefined');
if (teamSalaries == true) {

    var teamStats = document.getElementsByClassName("team_stats_1");
    var teamStatsValue = document.getElementsByClassName("team_stats_team_info_2");
    for (let i = 0; i < teamStatsValue.length; i++) console.log(teamStatsValue[i].innerText);
    var teamName = document.getElementsByClassName("team_stats_1_name");
    var valueElements = [1,2,4,5];
    for (let i = 0; i < 6; i++) {
        teamStatsValue[i].innerText = moneyToMillions(teamStatsValue[i]);
        if (valueElements.includes(i)) {
        teamStatsValue[i].parentNode.childNodes[1].style.marginRight = "-40px";
        if (teamStatsValue[i].innerText.length == 7) teamStatsValue[i].parentNode.childNodes[1].style.marginRight = "-49px";
        }

    }

    for (let i = 0; i < teamName.length; i++) {

        console.log(teamName[i].innerText.length);
        if (teamName[i].innerText.length > 17) {

            console.log(teamName[i].innerText);
            teamName[i].style.transform = "translateY(-6px)";
            console.log(teamName[i].parentNode.childNodes);
            //teamName[i].parentNode.childNodes[1].marginTop = "140px";

        }

    }

}

var leftTeam = !(typeof(left_team) === 'undefined');
if (leftTeam == true) {

    var playerOverall = document.getElementsByClassName("players_player_overall");
    for (let i = 0; i < playerOverall.length; i++) {

        playerOverall[i].style.color = "#fff";
        playerOverall[i] = skillsValuesColors(playerOverall[i]);


    }

    var playerPosition = document.getElementsByClassName("players_player_position");

    for (let i = 0; i < playerPosition.length; i++) {

        positionsColors(playerPosition[i]);

    }

    for (let i = 0; i < teamImages.length; i++) {
        console.log(clubs[i].name);

        teamImages[i+22].setAttribute("src", `/./static/images/club_logos/${clubs[i].name}.png`);
        //console.log(team_table_images[i].getAttribute("src"));
    }
}

var clubsDefined = !(typeof(clubs) === 'undefined');
if (clubsDefined == true) {
    for (let i = 0; i < teamImages.length; i++) {

        teamImages[i+20].setAttribute("src", `/./static/images/club_logos/${clubs[i].name}.png`);
        //console.log(team_table_images[i].getAttribute("src"));
    }

}


