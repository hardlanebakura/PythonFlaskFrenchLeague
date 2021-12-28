var teamImages = document.getElementsByTagName("img");
console.log(teamImages.length);

console.log(team);
var teamName = team.replaceAll(" ", "-");
console.log(teamName);
teamImages[10].setAttribute("src", `/./static/images/stadiums/stadium-${teamName}.jpg`);

var fifaToClubsDefined = !(typeof(fifaToClubs) === 'undefined');
if (fifaToClubsDefined == true) {

    console.log(fifaToClubs[team]);
    console.log(fifaToClubs);

    var tableTeam = document.getElementsByClassName("team_tables_table_team");
    var tableTeamName = document.getElementsByClassName("team_tables_table_team_name");
    console.log(teamsColors);
    for (let i = 0; i < tableTeamName.length; i++) {

        console.log(tableTeamName[i].innerText);
        for (var key in teamsColors) {

//            console.log(teamsColors[key]["name"]);
//            console.log(fifaToClubs[teamsColors[key]["name"]]);
//            console.log(fifaToClubs[teamsColors[key]["name"]]);
//            console.log(fifaToClubs[team]);
            if ((tableTeamName[i].innerText == fifaToClubs[teamsColors[key]["name"]]) && (fifaToClubs[teamsColors[key]["name"]] == fifaToClubs[team])) {

                var teamColors = teamsColors[key]["team_colors"];
                console.log(teamColors);
                var mainColor = teamColors[0];
                tableTeam[i].style.color = "#fff";
                if (mainColor !== "white") tableTeam[i].style.backgroundColor = mainColor;
                else tableTeam[i].style.backgroundColor = teamColors[1];
            }

        }

    }

}

var clubsDefined = !(typeof(clubs) === 'undefined');
console.log(clubsDefined);
if (clubsDefined == true) {
    for (let i = 0; i < teamImages.length; i++) {

        teamImages[i+12].setAttribute("src", `/./static/images/club_logos/${clubs[i].name}.png`);
        //console.log(team_table_images[i].getAttribute("src"));
    }

}

var playerOverallRating = document.getElementsByClassName("player_squad_player_overall");
var playerPotential = document.getElementsByClassName("player_squad_player_potential");

var tier1Skills = "#0c8539";
var tier2Skills = "#66a80f";
var tier3Skills = "#e6b600";
var tier4Skills = "#ff0000";

function changeColors(skillsValue) {

    console.log(parseInt(skillsValue.innerText));
    if (parseInt(skillsValue.innerText) > 79) skillsValue.style.backgroundColor = tier1Skills;
    else if (parseInt(skillsValue.innerText) > 69) skillsValue.style.backgroundColor = tier2Skills;
    else if (parseInt(skillsValue.innerText) > 59) skillsValue.style.backgroundColor = tier3Skills;
    else skillsValue.style.backgroundColor = tier4Skills;


}

for (let i = 0; i < playerOverallRating.length; i++) {

    changeColors(playerOverallRating[i]);
    changeColors(playerPotential[i]);

}