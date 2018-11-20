# Powershell command line interface to codewars.com

# See 
#  - http://dev.codewars.com/#api-reference
#  - example: https://github.com/shime/codewars

# Dependencies:
# - curl
# - ...


param(
#	[Parameter(Position=0)]
  	[ValidateSet('get','next','train','attempt')]
	[string]$action,
	[string]$kata_slug,
	$access_key, # taken from https://www.codewars.com/users/edit
	$language='csharp'
	)


if(test-path codewars.setup.ps1) { . .\codewars.setup.ps1 }

if(-not $access_key) { throw 'access_key required' }
else { "`$access_key='$access_key'" | sc codewars.setup.ps1 }

if($kata_slug) { 
	if( $kata_slug -notmatch '[a-zA-Z\-]+') { throw 'invalid kata_slug' }
	$kata_slug = $matches[0]
}

function start_kata($kata) { 
	$slug = $kata.slug

	if(-not (test-path "$slug*")) {
		$kata.description | sc -path "$slug.html"
		$d = $kata.session 
		$d = $d -replace '\@\{(projectId=\w+)\; (solutionId=\w+); setup=', 
			"/// Codewars kata: $($kata.name)`n/// `$1, `$2`n`n"
		$d = $d -replace '; exampleFixture=', "`n`n"
		$d = $d -replace '; code=\}', "`n`n"
		$d | sc "$slug.cs"
	}
	start "$slug.html"
	start gvim "$slug.cs"
}

switch($action) {
	'get' {
		if(-not $kata_slug) { throw 'kata_slug required' }
		$kata = (curl "https://www.codewars.com/api/v1/code-challenges/$kata_slug" -k -s | convertfrom-json)
		Write-Host $kata.description
	}
	'next' {
		$kata = (curl "https://www.codewars.com/api/v1/code-challenges/$language/train" `
		 -X POST `
		 -H "Authorization: $access_key" `
		 -d "strategy=default" `
		 -k -s | convertfrom-json)

		& start_kata $kata
	}
	'train' {
		if(-not $kata_slug) { throw 'kata_slug required' }

		curl "https://www.codewars.com/api/v1/code-challenges/$kata_slug/$language/train" `
		 -X POST `
		 -H "Authorization: $access_key" `
		 -k -s | convertfrom-json

	}
	'attempt' {
		if(-not $kata_slug) { throw 'kata_slug required' }

		$f = "$kata_slug.cs"
		if(-not (test-path $f)) { throw "kata code not found at '$f'" }
		$code = (gc $f) -join "`n" # gc -raw didn't work
		if($code -notmatch 'projectId=(\w+), solutionId=(\w+)') { throw "projectId and solutionId not found in '$f'" }
		$projectId = $matches[1]
		$solutionId = $matches[2]

		Write-Host 'sending attempt...'
		$code = $code -replace "`r",'' # CR breaks it
		$response = (curl `
			"https://www.codewars.com/api/v1/code-challenges/projects/$projectId/solutions/$solutionId/attempt" `
			 -X POST `
			 -d code=$code `
			 -H "Authorization: $access_key" `
			 -k -s | convertfrom-json)
		if(-not $response.success -or -not $response.dmid) { throw 'failed to get deffered message id for the attempt' }

		$count = 0
		$MAX_TRIES = 10; $SLEEP_SECONDS = 3
		$deferred = $null
		Write-Host 'waiting results...'
		while($true) {
			$deferred = (curl "https://www.codewars.com/api/v1/deferred/$($response.dmid)" `
				-H "Authorization: $access_key" `
				-k -s | convertfrom-json)

			if($deferred.success) { break }
			if($deferred.reason -eq 'not found') { throw 'invalid deferred message id' }
			sleep $SLEEP_SECONDS
			$count++
			if($count -eq $MAX_TRIES) { throw 'failed to get result of the attempt' }
		}

# TODO NEXT:
# FIX this:
# /tmp/csharp11676-17-k1fubf/code.cs(8,2): error CS1525: Unexpected symbol `end-of-file&#39;
# Error: Command failed: mcs -out:/tmp/csharp11676-17-k1fubf/test.dll -lib:/runner/frameworks/csharp/nunit -r:nunit.core.dll,nunit.core.interfaces.dll,nunit.util.dll,nunit.framework.dll -reference:System.Numerics.dll -reference:System.Drawing.dll -reference:System.Data.dll -reference:System.Messaging.dll -reference:System.Xml.dll -target:library -warn:2 /tmp/csharp11676-17-k1fubf/code.cs /tmp/csharp11676-17-k1fubf/fixture.cs
# /tmp/csharp11676-17-k1fubf/code.cs(8,2): error CS1525: Unexpected symbol `end-of-file&#39;
#
		Write-Host "result: `n$($deferred.reason)"
	}
}
