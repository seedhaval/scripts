function trashMail( qry ) {
  var threads = GmailApp.search( qry );
  for (var i = 0; i < threads.length; i++){
    threads[i].moveToTrash();
  }
}

function readMail( qry ) {
  var threads = GmailApp.search( qry );
  for (var i = 0; i < threads.length; i++){
    threads[i].markRead();
  }
}

function autoRead() {
  let ar = [
    ['paytm','2d'], ['amazon','2d'], ['dominos','2d']
  ];
  for( var j = 0; j < ar.length; j++ ){
    var qry = 'from:' + ar[j][0] + ' label:inbox older_than:' + ar[j][1];
    readMail( qry );
  }
}

function cleanFrom() {
  let ar = [
    ['paytm','90d'], ['amazon','30d'], ['nse_alerts','60d'],
    ['costaricachsl','2y'], ['commonfloor','2y'], ['adityabirlacapital','2y'],
    ['hdfcbank','2y'], ['tatasky','10d'], ['twitter','10d'],
    ['prameksol','10d'], ['ccavenue','10d'], ['mukeshmuthiyan','10d'],
    ['payback','10d'], ['infosys','2y'], ['birlasunlife','2y'],
    ['icicisecurities','2y'], ['payu','10d'], ['printvenue','10d'],
    ['lenskart','10d'], ['tumblr','10d'], ['ctnl','2y'],
    ['mahadiscom','1y'], ['sbilife','2y'], ['atomtech','10d'],
    ['indiangiftsportal','30d'], ['airtel','10d'], ['icicibank','2y'],
    ['goindigo','1y'], ['hdfcsec','2y'], ['roku','10d'],
    ['airpostmail','10d'], ['bsnl','2y'], ['seedhaval','2y'],
    ['gyanchandani','1y'],['dominos','30d'],
    ['vodafone','10d']
  ];
  for( var j = 0; j < ar.length; j++ ){
    var qry = 'from:' + ar[j][0] + ' older_than:' + ar[j][1];
    trashMail( qry );
  }
}

function autoClean(){
  cleanFrom();
  autoRead();
  trashMail( 'older_than:3y' );
}

