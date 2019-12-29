import taichi as ti

@ti.all_archs
def test_1d():
  return
  x = ti.var(ti.f32, shape=(16))

  @ti.kernel
  def func():
    for i in ti.ndrange((4, 10)):
      x[i] = i

  func()
  for i in range(16):
    if 4 <= i < 10:
      assert x[i] == i
    else:
      assert x[i] == 0


@ti.all_archs
def test_1d():
  ti.get_runtime().print_preprocessed = True
  ti.cfg.print_ir = True
  x = ti.var(ti.f32, shape=(16, 32))
  
  @ti.kernel
  def func():
    for i, j in ti.ndrange((4, 10), (3, 8)):
      x[i, j] = i + j * 10
  
  func()
  for i in range(16):
    for j in range(32):
      if 4 <= i < 10 and 3 <= j < 8:
        assert x[i] == i + j * 10
      else:
        assert x[i] == 0
