<?php

function buildArray($size) {
  // range already casts as array so array(range(0, $size)) would create nested array
  return range(0, $size);
}

function fyShuffle($input) {

  for ($i = count($input) - 1; $i >= 0; $i--) {
    $j = rand(0, count($input) - 1);

    $tmp = $input[$i];
    $input[$i] = $input[$j];
    $input[$j] = $tmp;
  }

  return $input;
}

function bogosort($input) {

  $attempts = 0;
  $sorted = true;

  do {

    $try = fyShuffle($input);
    $sorted = true;
    $attempts++;

    foreach ($try as $key => $value) {
      if ($key != $value) {
        $sorted = false;
      }
    }

  } while (!$sorted);

  return $attempts;
}


if ($argc <= 1) {
  throw new Exception('Missing input size.');
}

$tosort = fyShuffle(buildArray($argv[1]));
echo "Attempts: " . bogosort($tosort) . "\n";

?>
