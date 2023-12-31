var timer = document.getElementById('timer').innerHTML;
//console.log(timer);
timer = timer.replace(/[\[\]]/g, '', '"');
var lista = timer.split(',');

/*
console.log(lista);
console.log(typeof lista);
*/

simplyCountdown('#cuenta', {
	year: parseInt(lista[0]),//2025, // required
	month: 0 + parseInt(lista[1]), // required
	day: parseInt(lista[2]), // required
	hours: parseInt(lista[3]), // Default is 0 [0-23] integer
	minutes: parseInt(lista[4]), // Default is 0 [0-59] integer
	seconds: parseInt(lista[5]), // Default is 0 [0-59] integer
	words: { //words displayed into the countdown
		days: 'Día',
		hours: 'Hora',
		minutes: 'Minuto',
		seconds: 'Segundo',
		pluralLetter: 's'
	},
	plural: true, //use plurals
	inline: false, //set to true to get an inline basic countdown like : 24 days, 4 hours, 2 minutes, 5 seconds
	inlineClass: 'simply-countdown-inline', //inline css span class in case of inline = true
	// in case of inline set to false
	enableUtc: true, //Use UTC as default
	 //Callback on countdown end, put your own function here
	refresh: 1000, // default refresh every 1s
	sectionClass: 'simply-section', //section css class
	amountClass: 'simply-amount', // amount css class
	wordClass: 'simply-word', // word css class
	zeroPad: false,
	countUp: false
});