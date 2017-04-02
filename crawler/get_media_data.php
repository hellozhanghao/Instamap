<?php
/**
 * Created by PhpStorm.
 * User: zhanghao
 * Date: 2017/3/27
 * Time: 16:54
 */

//require('vendor/smochin/instagram-php-crawler/src/Crawler.php');
foreach (glob("vendor/*.php")as $filename){
    include $filename;
}


$crawler = new Smochin\Instagram\Crawler();
//$media = $crawler->getMediaByTag('z');
//print $media[1];
//$media = $crawler->getMediaByLocation(1163295);
//$media = $crawler->getMediaByTag('singapore');
//$tag = $crawler->getTag('f1');
//echo $media[0].getId();
//var_dump($media);
//print get_class($media[0]);
//
//
//print $media[1]->getCode();
//var_dump($media[1]->getTags());
//var_dump($media[1]->getLocation());
//print $media[1]->getCreated();
//print "\n";
//print $media[2]->getLocation()->getCoordinate();
//if ($media[2]->getLocation()->hasCoordinate()){
//    print "HAHAH";
//}else{
//    print "FSDF";
//}
//
//echo sizeof($media);
//


$input_file = fopen("instagram_locations.csv","r");
$output_file = fopen("instagram_data.csv", "w");

print_r(fgetcsv($input_file));
fputcsv($output_file,explode(',',"location_id,name,code,date_time"));


$count = 0;

while(! feof($input_file) ){
    try{
        $count++;
        print $count."\n";
        $row = fgetcsv($input_file);
        $location_id = $row[0];
        $name = $row[1];
        $media = $crawler->getMediaByLocation($location_id);
        foreach ($media as $photo){
            $code = $photo->getCode();
            $date_time = $photo->getCreated();
            $output_line = '';
            $output_line.= $location_id;
            $output_line.= ',';
            $output_line.= $name;
            $output_line.= ',';
            $output_line.= $code;
            $output_line.= ',';
            $output_line.= $date_time->format('Y-m-d H:i:s');
//        print_r($output_line);
//        print("\n");
            fputcsv($output_file,explode(',',$output_line));
        }
    }
    catch (Exception $e){
        print("Exception at ".$count."\n");
    }
}
