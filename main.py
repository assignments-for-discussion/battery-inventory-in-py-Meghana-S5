def count_batteries_by_health(present_capacities):
  SOH=100*present_capacity//120
  for i in present_capacities:
    if SOH>=80 and SOH<=100:
      health_count+=1
    elif SOH>=62 and SOH<=80:
      exchange_count+=1
    else:
      fail_count+=1

  return {
    "healthy": health_count,
    "exchange": exchange_count,
    "failed": fail_count
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
