$('.matcon').click(function () {
	let numId = +$(this).attr("one-num"),
		numType = $(this).attr("one-type");
	let isCheckId = appVue.chart[numId][numType + "Check"];
		
	if (appVue.chart[numId][numType + "Check"] == 'check_box') {
		// appVue[numType+"Check"][numId]='check_box_outline_blank';
		appVue.chart[numId][numType + "Check"] = 'check_box_outline_blank';
	} else {
		appVue.chart[numId][numType + "Check"] = 'check_box';
	}
});