$('.matcon').click(function () {
	let numId = +$(this).attr("one-num"),
		numType = $(this).attr("one-type");
	let isCheckId = appVue.chart[numId][numType + "Check"];
		
	if (isCheckId == 'check_box') {
		// appVue[numType+"Check"][numId]='check_box_outline_blank';
		isCheckId = 'check_box_outline_blank';
	} else {
		isCheckId = 'check_box';
	}
});