# whitelist-scripts

Scripts used to compile whitelists and merkle proofs for Art101 drops. Assumes you have [go-merkle-distributor](https://github.com/0xKiwi/go-merkle-distributor) installed to your system and you know how to use it.

The crux of these scripts is that I compile CSV files containing a wallet address and amount of tokens whitelisted for, and execute a series of Python scripts which generate the appropriate files needed for `go-merkle-distributor`. The scripts generate the merkle proofs and output needed which I host on the website as `distribution.json` and use client side Javascript to retrieve and parse proofs which then are used in the minting process on the website.

## Usage

For example's sake, let's say I have generated an export of holders of various tokens and stored it in `nfs.csv`, `mnd.csv`, and `bb.csv`. I update my `1_splice.py` script to reference those files after the `if __name__ == "__main__":` block. I execute `1_splice.py` which parses those CSV files and tallies up the amounts to each address and prints a JSON payload in the format needed for `go-merkle-distributor`.

```
$ python3 1_splice.py > output.json
```

From there, run `go-merkle-distributor` against `output.json` to generate the `addr-to-claim.json` file which contains the merkle proofs required for the merkle drop whitelist.

```
$ go-merkle-distributor --json-file=output.json
2020/12/25 01:27:55 Generating claim info for /home/lza_menace/git/github.com/art101nft/whitelist-scripts/output.json
2020/12/25 01:27:55 Root: 0x8f18c9e313036848cbbcb8b34676105ce866ee33bf29d16dee82bd1a8411163d
2020/12/25 01:27:55 Created claim info file at addr-to-claim.json
```

Now we need to setup the `distribution.json` which is the same file but cleaned up and the `root` proof removed. Idk how necessary this is tbh.

```
$ python3 2_striproot.py > ~/git/mywebsite.io/distribution.json
$ cd ~/git/mywebsite.io
$ git commit -am "updating merkle proof distribution file" && git push origin main
```

Run `3_tally.py` to return a total number of whitelisted addresses and amounts.

Pipe the output of `1_splice.py` into `jq` and use `grep` to search for specific accounts to see how much is allocated individually.
