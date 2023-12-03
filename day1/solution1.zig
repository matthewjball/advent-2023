const std = @import("std");
const mem = std.mem;

pub fn main() !void {
    var file = try std.fs.cwd().openFile("input.txt", .{});
    defer file.close();
    var buf_reader = std.io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();
    var buf: [1024]u8 = undefined;

    var sum: u16 = 0;
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        var cal_val: i8 = find_calibration_value(line);
        sum += cal_val;
    }

    std.debug.print("Total sum of calibration values: {s}\n", .{sum});
}

pub fn find_calibration_value(line: []const u8) i8 {
    // const allocator = std.heap.page_allocator;
    // const bytes = try allocator.alloc(u8, 100);
    // defer allocator.free(bytes);
    // var digits = std.ArrayList(u8).init(allocator);
    // defer digits.deinit();

    std.debug.print("{s}\n", .{line});
    for (line) |val| {
        if (std.ascii.isDigit(val)) {
            try digits.append(val);
        }
    }

    return 0;
}
