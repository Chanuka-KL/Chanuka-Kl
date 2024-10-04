function Monitor-NetworkConnectionsAdvanced {
    while ($true) {
        Clear-Host
        Write-Host "===== Advanced Network Connections Monitor =====" -ForegroundColor Cyan
        Write-Host "Proto | Local Address           | Remote Address          | State       | Process ID"
        Write-Host "-------------------------------------------------------------"

        # Get active network connections
        $connections = netstat -ano | Select-String "ESTABLISHED|LISTENING|TIME_WAIT"

        foreach ($connection in $connections) {
            $fields = $connection.ToString().Split(" ", [System.StringSplitOptions]::RemoveEmptyEntries)
            $proto = $fields[0]
            $localAddress = $fields[1]
            $remoteAddress = $fields[2]
            $state = $fields[3]
            $ProcID = $fields[4]  # Changed variable name from PID to ProcID

            # Color code based on connection state
            switch ($state) {
                "ESTABLISHED" { $color = "Green" }
                "LISTENING" { $color = "Yellow" }
                "TIME_WAIT" { $color = "Red" }
                default { $color = "White" }
            }

            Write-Host ("{0,-6} {1,-23} {2,-23} {3,-12} {4,-6}" -f $proto, $localAddress, $remoteAddress, $state, $ProcID) -ForegroundColor $color
        }

        Write-Host "===== Refreshing in 5 seconds... =====" -ForegroundColor Cyan
        Start-Sleep -Seconds 5
    }
}

Monitor-NetworkConnectionsAdvanced